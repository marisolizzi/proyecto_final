from django.shortcuts import render
from django.http import HttpResponse
from Usuario.forms import FormLogin, UserRegisterForm, UserEditForm
from django.contrib.auth.models import User
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
from Catalogo.models import Marca

# Create your views here.

def login_sitio(request):
    
    mensaje = ""

    if request.method=='POST':
        
        formulario = FormLogin(request.POST)
        
        if formulario.is_valid():
            
            usuario = request.POST["usuario"]
            clave = request.POST["password"]
            
            user = authenticate(request,username=usuario,password=clave)
            if user is not None:
                login(request,user)
                marcas = Marca.objects.all().order_by('nombre')
                cantidad = Marca.objects.count()
                contexto = {"mensaje":mensaje,"marcas":marcas,"cantidad":cantidad}
                return render(request,'Sitio/inicio.html',contexto)
            else:
                mensaje = "Datos incorrectos, por favor ingrésalos nuevamente."
                formulario = FormLogin()
                contexto = {"mensaje":mensaje,"formulario":formulario}
                return render(request,'Usuario/login.html',contexto)
        else:
            mensaje ="La información ingresada no es correcta. Inténtalo de nuevo!"
    else:
        formulario = FormLogin()

    contexto = {"mensaje":mensaje,"formulario":formulario}
    return render(request,'Usuario/login.html',contexto)

@login_required
def logout_sitio(request):
    
    logout(request)
    return render(request,'Usuario/logout.html')

@login_required
def lista_usuarios(request):
    mensaje =""
    usuarios = User.objects.all().order_by('username')
    cantidad = User.objects.count()
    contexto = {"mensaje":mensaje,"usuarios":usuarios,"cantidad":cantidad}
    return render(request,'Usuario/lista_usuarios.html',contexto)
    
@login_required
def nuevo_usuario(request):
    mensaje =""
    if request.method=='POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            username =  formulario.cleaned_data["username"]
            formulario.save()
            mensaje ="El Usuario se ingresó con éxito. Gracias!"
            usuarios = User.objects.all().order_by('username')
            cantidad = User.objects.count()
            contexto = {"mensaje":mensaje,"usuarios":usuarios,"cantidad":cantidad}
            return render(request,'Usuario/lista_usuarios.html',contexto)
        else:
            if formulario.errors:
                #messages.info(request, 'Input field errors:')
                mensaje+="Error en la validación del usuario:\n"
                for key, values in formulario.errors.as_data().items():
                    print("Bad value: %s - %s" % (key, values))
                    mensaje+=" %s - %s" % (key, values)
                    mensaje+="\n"
                contexto = {"mensaje":mensaje,"formulario":formulario}
                return render(request,'Usuario/nuevo_usuario.html',contexto)
    else:
        formulario = UserRegisterForm()
    contexto = {"mensaje":mensaje,"formulario":formulario}
    return render(request,'Usuario/nuevo_usuario.html',contexto)

@login_required
def editar_usuario(request,usuario_id):
    mensaje =""
    usuario = User.objects.get(id=usuario_id)
    
    usuario_actual = request.user
    if request.method=='POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
           info = formulario.cleaned_data
           usuario.password1=info['password1'],
           usuario.password2=info['password2'],
           usuario.email=info['email'],
           usuario.first_name=info['first_name'],
           usuario.last_name=info['last_name']
           usuario.username = usuario.username
           usuario.save()

           mensaje ="El Usuario se modificó con éxito. Gracias! "+usuario.last_name
           usuarios = User.objects.all().order_by('username')
           cantidad = User.objects.count()
           contexto = {"mensaje":mensaje,"usuarios":usuarios,"cantidad":cantidad}
           return render(request,'Usuario/lista_usuarios.html',contexto)
        else:
            if formulario.errors:
                #messages.info(request, 'Input field errors:')
                mensaje+="Error en la validación del usuario:\n"
                for key, values in formulario.errors.as_data().items():
                    print("Bad value: %s - %s" % (key, values))
                    mensaje+=" %s - %s" % (key, values)
                    mensaje+="\n"
                contexto = {"mensaje":mensaje,"formulario":formulario,"usuario":usuario}
                return render(request,'Usuario/editar_usuario.html',contexto)
    else:
        formulario = UserEditForm(initial={"email":usuario.email,"first_name":usuario.first_name,"last_name":usuario.last_name})
    contexto = {"mensaje":mensaje,"formulario":formulario,"usuario":usuario}
    return render(request,'Usuario/editar_usuario.html',contexto)

@login_required
def eliminar_usuario(request,usuario_id):
    mensaje =""
    usuario = User.objects.get(id=usuario_id)
    usuario.delete()
    mensaje ="El Usuario se eliminó con éxito. Gracias!"
    usuarios = User.objects.all().order_by('username')
    cantidad = User.objects.count()
    contexto = {"mensaje":mensaje,"usuarios":usuarios,"cantidad":cantidad}
    return render(request,'Usuario/lista_usuarios.html',contexto)

