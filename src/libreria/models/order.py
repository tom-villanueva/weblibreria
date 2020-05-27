from django.db import models
from django.contrib.auth import get_user_model
from libreria.models import Book

User = get_user_model()

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Book, on_delete=models.CASCADE)