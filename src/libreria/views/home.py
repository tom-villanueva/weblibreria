from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from libreria.models import Book 

# Create your views here.

class VistaHome(TemplateView):
    template_name = 'libreria/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        
        context['book_list'] = Book.objects.all()
        context['book_list_sale'] = Book.objects.filter(sale__isnull=False)[:3]      
        return context


