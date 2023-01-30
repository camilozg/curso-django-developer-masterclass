# from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

#Urls dinámicas

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 GENERIC ERROR") # 404.html

def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2 -> num1 + num2
    result = num1 + num2
    return HttpResponse(str(result))

# domain.com/first_app/0 -> domain.com/first_app/sports

def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]
    return HttpResponseRedirect(reverse('topic-page', args = [topic]))

def simple_view(request):
    # En caso de crear el directorio de templates al nivel del proyecto
    # hay que agregar la ruta en las settings del proyecto
    # SETTINGS > TEMPLATES > DIRS: os.path.join(BASE_DIR,'templates/')
    return render(request,'first_app/example.html') 

#Urls estáticas
 
# def sports_view(request):
#     return HttpResponse("Sports Page")

# def finance_view(request):
#     return HttpResponse("Finance Page") 