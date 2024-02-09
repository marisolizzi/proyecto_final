from django.urls import path
from Sitio import views


urlpatterns = [
    path('', views.inicio, name="Home"),
    path('marca/<marca_id>', views.marca, name="Marca"),
    path('modelo/<celular_id>', views.celular, name="Celular"),
    path('acerca/', views.acerca, name="AcercaDe"),
]