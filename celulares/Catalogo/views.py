from django.shortcuts import render
from django.http import HttpResponse
#from Catalogo.forms import FormCurso,FormEstudiante,FormProfesor,FormEntregable,FormBuscador
#from App1.models import Curso,Estudiante,Profesor,Entregable

# Create your views here.

def inicio(request):
    return render(request,'Catalogo/inicio.html')

