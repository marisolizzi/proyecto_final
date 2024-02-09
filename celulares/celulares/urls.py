"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from celulares.views import saludo
from Sitio.views import inicio
from Usuario.views import login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Sitio.urls')),
    path('catalogo/', include('Catalogo.urls')),
    path('usuario/', include('Usuario.urls')),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)