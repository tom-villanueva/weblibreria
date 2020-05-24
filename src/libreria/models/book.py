from django.db import models

class Book(models.Model):

    SALE_CHOICES = [
        ('C', '5%'),
        ('D', '10%'),
        ('Q', '15%'),
        ('V', '20%'),
    ]

    title = models.CharField(max_length=255)
    isbn = models.BigIntegerField()
    sinposis = models.CharField(max_length=255)
    price = models.FloatField()
    sale = models.CharField(max_length=1 ,choices=SALE_CHOICES)
    
     
