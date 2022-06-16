from operator import mod
from django.db import models

# Create your models here.
class Enterprise(models.Model):
    unique_id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=200, default="chamaco")
    telephone = models.IntegerField(max_length=15, default=0)
    def __str__(self):
        return self.name

class Product(models.Model):
    idem = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, default="nombre_no_registrado")
    propietary = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    unitary_price = models.FloatField(default=0)
    quantity = models.PositiveBigIntegerField(default=0)
    color = models.CharField(max_length=200, default="chamaco")
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    grosor = models.FloatField(default=0)
    def __str__(self):
        return self.name
    