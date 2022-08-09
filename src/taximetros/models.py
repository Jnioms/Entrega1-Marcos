from django.db import models

# Create your models here.
class Taximetro(models.Model):

    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"