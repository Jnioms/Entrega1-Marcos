from django.http import HttpResponse
from django.shortcuts import redirect, render
from taximetros.models import Taximetro
from taximetros.forms import CrearTaximetro, BuscarTaximetro

# Create your views here.

def index(request):

    listado_taximetros = Taximetro.objects.all()

    if request.GET.get("nombre_buscar"):
        
        formulario = BuscarTaximetro(request.GET)
        
        if formulario.is_valid():
            
            data = formulario.cleaned_data

            listado_taximetros = listado_taximetros.filter(nombre__icontains = data.get("nombre_buscar"))
    
        return render(request,"taximetros/index.html", {"basedatos": listado_taximetros, "formulario": formulario})

    else:

        formulario = BuscarTaximetro()
        return render(request,"taximetros/index.html", {"basedatos": listado_taximetros, "formulario": formulario})

def crear(request):

    if request.method == "GET":
        
        formulario = CrearTaximetro()
        
        return render(request, "taximetros/crear.html", {"formulario": formulario})
    
    else:
        
        formulario = CrearTaximetro(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            nombre = data.get("nombre")
            precio = data.get("precio")
            descripcion = data.get("descripcion")
            stock = data.get("stock")

            taximetro = Taximetro(nombre=nombre, precio=precio, descripcion=descripcion, stock=stock)
            taximetro.save()

            return redirect('taximetros_index')

        else:

            return HttpResponse("El taximetro no pudo ser creado.")