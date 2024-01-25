from django.urls import path
from Catalogo import views


urlpatterns = [
    path('', views.inicio, name="Home"),
]