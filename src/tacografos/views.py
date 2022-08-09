from django.http import HttpResponse
from django.shortcuts import redirect, render
from tacografos.models import Tacografo
from tacografos.forms import CrearTacografo, BuscarTacografo

# Create your views here.

def index(request):

    listado_tacografos = Tacografo.objects.all()

    if request.GET.get("nombre_buscar"):
        
        formulario = BuscarTacografo(request.GET)
        
        if formulario.is_valid():
            
            data = formulario.cleaned_data

            listado_tacografos = listado_tacografos.filter(nombre__icontains = data.get("nombre_buscar"))
    
        return render(request,"tacografos/index.html", {"basedatos": listado_tacografos, "formulario": formulario})

    else:

        formulario = BuscarTacografo()
        return render(request,"tacografos/index.html", {"basedatos": listado_tacografos, "formulario": formulario})

def crear(request):

    if request.method == "GET":
        
        formulario = CrearTacografo()
        
        return render(request, "tacografos/crear.html", {"formulario": formulario})
    
    else:
        
        formulario = CrearTacografo(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            nombre = data.get("nombre")
            precio = data.get("precio")
            descripcion = data.get("descripcion")
            stock = data.get("stock")

            tacografo = Tacografo(nombre=nombre, precio=precio, descripcion=descripcion, stock=stock)
            tacografo.save()

            return redirect('tacografos_index')

        else:

            return HttpResponse("El tacografo no pudo ser creado.")