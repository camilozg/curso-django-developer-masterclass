from django.shortcuts import render

# Create your views here.

def example_view(request):
    # En caso de crear el directorio de templates al nivel del app que es lo más recomendable
    # hay que crear dentro otro directorio con el nombre del app "templates/my_app/template.html"
    # para que las plantillas se puedan diferenciar de otras con el mismo nombre en otras aplicaciones
    # También hay que agregar en las settings del proyecto la clase de configuración del app
    # ubicado en apps.py para que Django sepa que debe buscar templates en esa app
    # SETTINGS > INSTALLED_APPS['my_app.apps.MyAppConfig']
    return render(request,'my_app/example.html')

def variable_view(request):

    my_var = {
        'first_name': 'Camilo',
        'last_name': 'Zamora',
        'some_list':['A','B','C'],
        'some_dict':{'inside_key':'inside_value'},
        'user_logged_in': True
        }

    return render(request, 'my_app/variable.html', context = my_var)

def example_inheritance_view(request):
    return render(request, "my_app/example_inheritance.html")