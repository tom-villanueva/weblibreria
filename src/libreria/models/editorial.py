from django.db import models

class Editorial(models.Model):
    editorial_name = models.CharField(max_length=255)
    