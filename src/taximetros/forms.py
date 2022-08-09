from typing import Text
from django.forms import Form, CharField, FloatField, Textarea, IntegerField

class CrearTaximetro(Form):

    nombre = CharField(max_length=100)
    precio = FloatField()
    descripcion = CharField(widget=Textarea())
    stock = IntegerField()

class BuscarTaximetro(Form):
    
    nombre_buscar = CharField(max_length=100, required=False)