from django.views.generic.detail import DetailView
from libreria.models.book import Book 

class BookDetailView(DetailView):
    model = Book
