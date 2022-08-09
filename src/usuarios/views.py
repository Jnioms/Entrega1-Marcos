from django.http import HttpResponse
from django.shortcuts import redirect, render
from usuarios.models import Usuario
from usuarios.forms import CrearUsuario, BuscarUsuario

# Create your views here.

def index(request):

    listado_usuarios = Usuario.objects.all()

    if request.GET.get("nombre_buscar"):
        
        formulario = BuscarUsuario(request.GET)
        
        if formulario.is_valid():
            
            data = formulario.cleaned_data

            listado_usuarios = listado_usuarios.filter(nombre__icontains = data.get("nombre_buscar"))
    
        return render(request,"usuarios/index.html", {"basedatos": listado_usuarios, "formulario": formulario})

    else:

        formulario = BuscarUsuario()
        return render(request,"usuarios/index.html", {"basedatos": listado_usuarios, "formulario": formulario})

def crear(request):

    if request.method == "GET":
        
        formulario = CrearUsuario()
        
        return render(request, "usuarios/crear.html", {"formulario": formulario})
    
    else:
        
        formulario = CrearUsuario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            nombre = data.get("nombre")
            user_pass = data.get("user_pass")
            mail = data.get("mail")
            dist_tax = data.get("dist_tax")
            dist_tac = data.get("dist_tac")

            usuario = Usuario(nombre=nombre, user_pass=user_pass, mail=mail, dist_tax=dist_tax, dist_tac=dist_tac)
            usuario.save()

            return redirect('usuario_index')

        else:

            return HttpResponse("El usuario no pudo ser creado.")