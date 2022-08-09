from django.forms import Form, CharField, EmailField, BooleanField, PasswordInput

class CrearUsuario(Form):

    nombre = CharField(max_length=100)
    user_pass = CharField(max_length=50, widget=PasswordInput())
    mail = EmailField()
    dist_tax = BooleanField(required=False)
    dist_tac = BooleanField(required=False)

class BuscarUsuario(Form):
    
    nombre_buscar = CharField(max_length=100, required=False)