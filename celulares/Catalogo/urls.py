from django.urls import path
from Catalogo import views


urlpatterns = [
    path('lista-marcas/', views.lista_marcas, name="Lista Marcas"),
    path('nueva-marca/', views.nueva_marca, name="Nueva Marca"),
    path('editar-marca/<marca_id>', views.editar_marca, name="Editar Marca"),
    path('eliminar-marca/<marca_id>', views.eliminar_marca, name="Eliminar Marca"),
    path('lista-celulares/', views.lista_celulares, name="Lista Celulares"),
    path('nuevo-celular/', views.nuevo_celular, name="Nuevo Celular"),
    path('editar-celular/<celular_id>', views.editar_celular, name="Editar Celular"),
    path('eliminar-celular/<celular_id>', views.eliminar_celular, name="Eliminar Celular"),
]
