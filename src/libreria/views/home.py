from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.

class VistaHome(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
