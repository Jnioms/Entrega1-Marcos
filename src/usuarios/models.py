from django.db import models

# Create your models here.
class Usuario(models.Model):

    nombre = models.CharField(max_length=100)
    user_pass = models.CharField(max_length=50)
    mail = models.EmailField()
    dist_tax = models.BooleanField()
    dist_tac = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} - {self.mail}"