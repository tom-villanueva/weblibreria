from django.urls import path
from libreria.views import VistaHome

urlpatterns = [
    path('', VistaHome.as_view()),
]
