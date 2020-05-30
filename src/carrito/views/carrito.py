from django.views.generic import DetailView
from carrito.models import Carrito

class CarritoDetailView(DetailView):
    template_name = 'carrito/carrito_detail.html' 
    model = Carrito