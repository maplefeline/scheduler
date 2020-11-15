#!/usr/bin/env bash
# deploys git head branch to heroku app
# make sure to commit changes before running, working tree changes will not be picked up
# this is not intended for production deployment, that should follow git action workflow
#
### Usage:
# ./deploy-heroku.sh '<heroku-app-name>'
#
## drop database before release, implies migrate database too
# ./deploy-heroku.sh --drop-db '<heroku-app-name>'
#
## migrate database after release
# ./deploy-heroku.sh --migrate-db '<heroku-app-name>'

set -o pipefail
set -ex

cleanup() {
  set +e
  if [ -n "${git_remote}" ]; then
    git remote remove heroku
    git remote rename "${git_remote}" heroku
  fi
}

trap cleanup EXIT

drop_db='false'
migrate_db='false'
git_remote=

while true; do
  case "$1" in
    '--drop-db' )
      drop_db='true'
      migrate_db='true'
      ;;
    '--migrate-db' )
      migrate_db='true'
      ;;
    * )
      break
      ;;
  esac
  shift
done

SCHEDULER_ALLOWED_HOSTS="$(
  jq -c -n \
  --argjson scheduler_allowed_hosts "${SCHEDULER_ALLOWED_HOSTS:-[]}" \
  --arg allowed_host "$1.herokuapp.com" \
  '$scheduler_allowed_hosts + [$allowed_host]'
)"

if git remote | grep heroku; then
  git_remote="heroku-${RANDOM}"
  if ! git remote rename heroku "${git_remote}"; then
    # probably missing remote named exactly 'heroku', in which case the script is non-destructive
    git_remote=
  fi
fi

if [ "${drop_db}" = 'true' ]; then
  heroku pg:reset DATABASE -a "$1"
fi

heroku config:set DISABLE_COLLECTSTATIC=1 -a "$1"
heroku config:set SCHEDULER_ALLOWED_HOSTS="${SCHEDULER_ALLOWED_HOSTS:-[]}" -a "$1"
heroku git:remote -a "$1"

branch="$(git branch | grep -F -e '* ' | cut -d' ' -f2)"

git push heroku "${branch}:main" --force

if [ "${migrate_db}" = 'true' ]; then
  heroku run -a "$1" -x -- python scheduler/manage.py migrate
fi
