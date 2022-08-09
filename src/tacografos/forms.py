from typing import Text
from django.forms import Form, CharField, FloatField, Textarea, IntegerField

class CrearTacografo(Form):

    nombre = CharField(max_length=100)
    precio = FloatField()
    descripcion = CharField(widget=Textarea())
    stock = IntegerField()

class BuscarTacografo(Form):
    
    nombre_buscar = CharField(max_length=100, required=False)