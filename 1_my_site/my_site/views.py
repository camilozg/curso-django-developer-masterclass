from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return HttpResponse("HOME VIEW")

def my_custom_page_not_found_view(request, exception):
    return render(request, '404_custom_name.html', status = 404)