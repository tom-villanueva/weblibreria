from django.views.generic import ListView
from libreria.models.book import Book

class BookListView(ListView):
    model = Book 

    def get(self, request, *args, **kwargs):
        self.genero = self.kwargs['slug']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genero'] = self.genero
        return context

    def get_queryset(self):
        return Book.objects.filter(genre = self.genero)[:5]