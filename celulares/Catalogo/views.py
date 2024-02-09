from django.shortcuts import render
from django.http import HttpResponse
from Catalogo.forms import FormMarca,FormCelular
from Catalogo.models import Marca, Celular
from django.contrib.auth.decorators import login_required

# ////////////////////////////////////////////////
# MARCAS
#/////////////////////////////////////////////////

@login_required
def lista_marcas(request):
    mensaje =""
    marcas = Marca.objects.all().order_by('nombre')
    cantidad = Marca.objects.count()
    contexto = {"mensaje":mensaje,"marcas":marcas,"cantidad":cantidad}
    return render(request,'Catalogo/lista_marcas.html',contexto)

@login_required
def nueva_marca(request):
    mensaje =""
    if request.method=='POST':
        formulario = FormMarca(request.POST,request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            marca_u = Marca(nombre=info['nombre'],detalle=info['detalle'],imagen=info['imagen'])
            marca_u.save()
            mensaje ="La Marca se ingresó con éxito. Gracias!"
            marcas = Marca.objects.all().order_by('nombre')
            cantidad = Marca.objects.count()
            contexto = {"mensaje":mensaje,"marcas":marcas,"cantidad":cantidad}
            return render(request,'Catalogo/lista_marcas.html',contexto)
        else:
            mensaje ="La información ingresada no es correcta. Inténtalo de nuevo!"
            marcas = Marca.objects.all().order_by('nombre')
            cantidad = Marca.objects.count()
            contexto = {"mensaje":mensaje,"marcas":marcas,"cantidad":cantidad}
            return render(request,'Catalogo/lista_marcas.html',contexto)
    else:
        formulario = FormMarca()
    contexto = {"mensaje":mensaje,"formulario":formulario}
    return render(request,'Catalogo/nueva_marca.html',contexto)

@login_required
def editar_marca(request,marca_id):
    mensaje =""
    marca = Marca.objects.get(id=marca_id)
    
    if request.method=='POST':
        formulario = FormMarca(request.POST,request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data

            nueva_img = info['imagen']
            if nueva_img == None:
                nueva_img = marca.imagen

            marca_u = Marca(
                id=marca.id,
                nombre=info['nombre'],
                detalle=info['detalle'],
                imagen=nueva_img)
            marca_u.save()
            mensaje ="La Marca se editó con éxito. Gracias!"
            marcas = Marca.objects.all().order_by('nombre')
            cantidad = Marca.objects.count()
            contexto = {"mensaje":mensaje,"marcas":marcas,"cantidad":cantidad}
            return render(request,'Catalogo/lista_marcas.html',contexto)
        else:
            mensaje ="La información ingresada no es correcta. Inténtalo de nuevo!"
            marcas = Marca.objects.all().order_by('nombre')
            cantidad = Marca.objects.count()
            contexto = {"mensaje":mensaje,"marcas":marcas,"cantidad":cantidad}
            return render(request,'Catalogo/lista_marcas.html',contexto)
    else:
        formulario = FormMarca(initial={"id":marca.id,"nombre":marca.nombre,"detalle":marca.detalle,"imagen":marca.imagen})

    contexto = {"mensaje":mensaje,"formulario":formulario,"marca":marca}
    return render(request,'Catalogo/editar_marca.html',contexto)

@login_required
def eliminar_marca(request,marca_id):
    mensaje =""
    marca = Marca.objects.get(id=marca_id)
    marca.delete()
    mensaje ="La Marca se eliminó con éxito. Gracias!"
    marcas = Marca.objects.all().order_by('nombre')
    cantidad = Marca.objects.count()
    contexto = {"mensaje":mensaje,"marcas":marcas,"cantidad":cantidad}
    return render(request,'Catalogo/lista_marcas.html',contexto)

# ////////////////////////////////////////////////
# CELULARES
#/////////////////////////////////////////////////

@login_required
def lista_celulares(request):
    mensaje =""
    celulares = Celular.objects.all().order_by('nombre')
    cantidad = Celular.objects.count()
    contexto = {"mensaje":mensaje,"celulares":celulares,"cantidad":cantidad}
    return render(request,'Catalogo/lista_celulares.html',contexto)

@login_required
def nuevo_celular(request):
    mensaje =""
    if request.method=='POST':
        formulario = FormCelular(request.POST,request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            marca_u = Celular(categoria=info['categoria'],nombre=info['nombre'],detalle=info['detalle'],imagen=info['imagen'])
            marca_u.save()
            mensaje ="El Celular se ingresó con éxito. Gracias!"
            celulares = Celular.objects.all().order_by('nombre')
            cantidad = Celular.objects.count()
            contexto = {"mensaje":mensaje,"celulares":celulares,"cantidad":cantidad}
            return render(request,'Catalogo/lista_celulares.html',contexto)
        else:
            mensaje ="La información ingresada no es correcta. Inténtalo de nuevo!"
            celulares = Celular.objects.all().order_by('nombre')
            cantidad = Celular.objects.count()
            contexto = {"mensaje":mensaje,"celulares":celulares,"cantidad":cantidad}
            return render(request,'Catalogo/lista_celulares.html',contexto)
    else:
        formulario = FormCelular()
    contexto = {"mensaje":mensaje,"formulario":formulario}
    return render(request,'Catalogo/nuevo_celular.html',contexto)

@login_required   
def editar_celular(request,celular_id):
    mensaje =""
    celular = Celular.objects.get(id=celular_id)
    
    if request.method=='POST':
        formulario = FormCelular(request.POST,request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            nueva_img = info['imagen']
            if nueva_img == None :
                nueva_img = celular.imagen

            celular_u = Celular(
                id=celular.id,
                nombre=info['nombre'],
                categoria=info['categoria'],
                detalle=info['detalle'],
                imagen=nueva_img)

            celular_u.save()
            mensaje ="El Celular se editó con éxito. Gracias!"
            celulares = Celular.objects.all().order_by('nombre')
            cantidad = Celular.objects.count()
            contexto = {"mensaje":mensaje,"celulares":celulares,"cantidad":cantidad}
            return render(request,'Catalogo/lista_celulares.html',contexto)
        else:
            mensaje ="La información ingresada no es correcta. Inténtalo de nuevo!"
            celulares = Celular.objects.all().order_by('nombre')
            cantidad = Celular.objects.count()
            contexto = {"mensaje":mensaje,"celulares":celulares,"cantidad":cantidad}
            return render(request,'Catalogo/lista_celulares.html',contexto)
    else:
        formulario = FormCelular(initial={"id":celular.id,"categoria":celular.categoria,"nombre":celular.nombre,"detalle":celular.detalle,"imagen":celular.imagen})

    contexto = {"mensaje":mensaje,"formulario":formulario,"celular":celular}
    return render(request,'Catalogo/editar_celular.html',contexto)

@login_required
def eliminar_celular(request,celular_id):
    mensaje =""
    marca = Celular.objects.get(id=celular_id)
    marca.delete()
    mensaje ="El Celular se eliminó con éxito. Gracias!"
    celulares = Celular.objects.all().order_by('nombre')
    cantidad = Celular.objects.count()
    contexto = {"mensaje":mensaje,"celulares":celulares,"cantidad":cantidad}
    return render(request,'Catalogo/lista_celulares.html',contexto)
