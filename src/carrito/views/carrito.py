from django.views.generic import DetailView
from carrito.models import Carrito
from django.contrib.auth.mixins import LoginRequiredMixin

class CarritoDetailView(LoginRequiredMixin, DetailView):
    template_name = 'carrito/carrito_detail.html' 
    model = Carrito

    login_url = '/users/login/'

    def get(self, request, *args, **kwargs):
        self.carrito_id = request.user.carrito.id
        print(self.carrito_id)
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return Carrito.objects.get(id=self.carrito_id)
