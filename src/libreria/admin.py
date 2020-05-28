from django.contrib import admin
from libreria.models import Book, Genre, Author, Editorial 

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Editorial)