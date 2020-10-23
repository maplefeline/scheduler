"""
WSGI config for scheduler project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

from os import environ

from django.core.wsgi import get_wsgi_application  # type: ignore

environ.setdefault("DJANGO_SETTINGS_MODULE", "scheduler.settings")

application = get_wsgi_application()