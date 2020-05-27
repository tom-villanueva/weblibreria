from django.urls import path
from libreria.views.home import VistaHome
from libreria.views.bookdetailview import BookDetailView

urlpatterns = [
    path('', VistaHome.as_view(), name='home'),
    path('Libro/<int:pk>', BookDetailView.as_view(), name='bookview')
]
