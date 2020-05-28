from django.urls import path
from libreria.views.home import VistaHome
from libreria.views.bookdetailview import BookDetailView
from libreria.views.genrelistview import GenreListView

urlpatterns = [
    path('', VistaHome.as_view(), name='home'),
    path('Libro/<int:pk>', BookDetailView.as_view(), name='book-view'),
    path('Generos/', GenreListView.as_view(), name='genre-list-view'), 
]
