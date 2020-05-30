from django.urls import path
from carrito.views import CarritoDetailView

urlpatterns = [
    path('', CarritoDetailView.as_view(), name='carrito-detail'),
]
