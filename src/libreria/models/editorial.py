from django.db import models

class Editorial(models.Model):
    editorial_name = models.CharField(max_length=255)
    
    class Meta():
        ordering = ['editorial_name']

    def __str__(self):
        return self.editorial_name