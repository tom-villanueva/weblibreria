from django.db import models
from django.urls import reverse

class Genre(models.Model):
    genre_name = models.CharField(max_length=255)

    class Meta():
        ordering = ['genre_name']
    
    #def get_absolute_url(self):
        #return reverse('', args=[str(self.id)])

    def __str__(self):
        return self.genre_name
