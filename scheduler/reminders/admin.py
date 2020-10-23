from django.contrib import admin  # type: ignore

from .models import Reminder

admin.site.register(Reminder)
