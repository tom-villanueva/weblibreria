from django.views.generic import ListView
from libreria.models.book import Book

class BookListView(ListView):
    model = Book 