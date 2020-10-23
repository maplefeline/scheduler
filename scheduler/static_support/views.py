from django.http import HttpResponse  # type: ignore
from django.views import View  # type: ignore
from django.views.generic import TemplateView  # type: ignore


class Favicon(View):
    http_method_names = ["get", "head", "options", "trace"]

    def get(self, request: object, *args: object, **kwargs: object) -> object:
        return HttpResponse()


class IndexView(TemplateView):
    template_name = "static_support/index.html.j2"
