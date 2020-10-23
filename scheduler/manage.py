#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
from os import environ
from sys import argv

try:
    from django.core.management import execute_from_command_line  # type: ignore
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc


if __name__ == "__main__":
    environ.setdefault("DJANGO_SETTINGS_MODULE", "scheduler.settings")
    execute_from_command_line(argv)
