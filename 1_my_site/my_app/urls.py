from django.urls import path
from . import views

# registrar el namespace de la app con la variable especial app_name
# así podemos usar los nombres de las rutas en las plantillas html 
app_name = 'my_app'

urlpatterns = [
    path('', views.example_view, name = 'example'),
    path('variable/', views.variable_view, name = 'variable'),
    path('example_inh/', views.example_inheritance_view,  name = 'example_inh')
]
