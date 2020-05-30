from django.urls import path
from libreria.views.home import VistaHome
from libreria.views import BookDetailView, GenreListView, BookListView

urlpatterns = [
    path('', VistaHome.as_view(), name='home'),
    path('Libro/<int:pk>/', BookDetailView.as_view(), name='book-view'),
    path('Generos/', GenreListView.as_view(), name='genre-list-view'),
    path('Generos/<slug:slug>/', BookListView.as_view(), name='book-list-view'),  
]
