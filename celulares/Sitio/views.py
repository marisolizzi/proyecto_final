from django.shortcuts import render
from django.http import HttpResponse
from Catalogo.models import Marca, Celular
import re

# Create your views here.
def inicio(request):
    mensaje =""
    marcas = Marca.objects.all().order_by('nombre')
    cantidad = Marca.objects.count()
    contexto = {"mensaje":mensaje,"marcas":marcas,"cantidad":cantidad}
    return render(request,'Sitio/inicio.html',contexto)

def acerca(request):
    return render(request,'Sitio/acerca.html')

def marca(request,marca_id):
    mensaje =""
    marca = Marca.objects.get(id=marca_id)
    titulo = "Modelos en "+marca.nombre
    if request.method=='POST':
        busqueda = strip_tags(request.POST['search'])
        celulares = Celular.objects.filter(nombre__icontains=busqueda,categoria=marca_id)
        cantidad = celulares.count()
        titulo = "Buscando \""+busqueda+"\" en "+marca.nombre
        contexto = {"mensaje":mensaje,"celulares":celulares,"cantidad":cantidad,"marca":marca,"titulo":titulo,"reset":True}
        return render(request,'Sitio/marca.html',contexto)

    celulares = Celular.objects.filter(categoria=marca_id).values().order_by('nombre')
    cantidad = Celular.objects.filter(categoria=marca_id).values().count()
    contexto = {"mensaje":mensaje,"celulares":celulares,"cantidad":cantidad,"marca":marca,"titulo":titulo,"reset":False}
    return render(request,'Sitio/marca.html',contexto)

def celular(request,celular_id):
    mensaje =""
    celular = Celular.objects.get(id=celular_id)
    marca = Marca.objects.get(id=celular.categoria)
    contexto = {"mensaje":mensaje,"marca":marca,"celular":celular}
    return render(request,'Sitio/celular.html',contexto)

def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value)