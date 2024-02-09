from django.urls import path
from Usuario import views

urlpatterns = [
    path('login/', views.login_sitio, name="Login"),
    path('logout/', views.logout_sitio, name="Logout"),
    path('lista-usuarios/', views.lista_usuarios, name="Lista Usuarios"),
    path('nuevo-usuario/', views.nuevo_usuario, name="Nuevo Usuario"),
    path('editar-usuario/<usuario_id>', views.editar_usuario, name="Editar Usuario"),
    path('eliminar-usuario/<usuario_id>', views.eliminar_usuario, name="Eliminar Usuario"),
]