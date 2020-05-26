from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=255)

    class Meta():
        ordering = ['genre_name']

    def __str__(self):
        return self.genre_name
