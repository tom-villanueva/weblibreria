from django.views.generic.detail import DetailView
from libreria.models.book import Book 
from django.forms import Form
from django.shortcuts import render
from carrito.models import Carrito

class BookDetailView(DetailView):
    model = Book
    form_class = Form
    template_name = 'libreria/book_detail.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            libro_id = self.kwargs['pk']
            libro = Book.objects.get(id=libro_id)
            print(libro)
            #Con el request.user.carrito
            carrito = request.user.carrito
            #carrito = Carrito.objects.get(id=carrito_id)
            print('Carrito: ')
            print(carrito.id)
            carrito.productos.add(libro)
            #Hacer relacion



            #return HttpResponseRedirect('/success/')
            return render(request, self.template_name, {'form': form})
            #return libro
        else:
            return render(request, self.template_name, {'form': form})