"""
ASGI config for scheduler project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

from os import environ

from django.core.asgi import get_asgi_application  # type: ignore

environ.setdefault("DJANGO_SETTINGS_MODULE", "scheduler.settings")

application = get_asgi_application()
