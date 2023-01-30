"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),
    path('my_app/', include('my_app.urls')),
    path('office/', include('office.urls')),
    path('', views.home_view, name='home')
]

# variable reservada para asignar una view que llama el template de error 404 con un nombre personalizado
# si no se asigna usará el template con el nombre por defecto 404.html
# es recomendable crear la view y asignar la variable incluso si se vaya a usar el nombre por defecto
# para ver el template de error 404 hay que desactivar el modo debug en las settings del proyecto
handler404 = 'my_site.views.my_custom_page_not_found_view'
