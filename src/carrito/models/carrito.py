from django.db import models
from libreria.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()

class Carrito(models.Model):
    cliente = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Book)
    actualizado = models.DateTimeField(auto_now=True)