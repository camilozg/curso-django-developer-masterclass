from email import contentmanager
from django.shortcuts import render
from . import models 

# Create your views here.

def list_patients(request):

    all_patients = models.Patient.objects.all()
    list = {'patients':all_patients}

    return render(request, 'office/list.html', context = list)