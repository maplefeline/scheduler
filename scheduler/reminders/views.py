from django.views.generic.detail import DetailView  # type: ignore
from django.views.generic.list import ListView  # type: ignore

from .models import Reminder


class ReminderDetailView(DetailView):
    model = Reminder
    pk_url_kwarg = "id"


class ReminderListView(ListView):
    model = Reminder
    paginate_by = 1000
