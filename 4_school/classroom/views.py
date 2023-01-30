from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Teacher
from . import forms
from django.urls import reverse_lazy

# Create your views here.

# Function based view


def home_view(request):
    return render(request, 'classroom/home.html')

# Class based views


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ContactFormView(FormView):
    form_class = forms.ContactForm
    template_name = 'classroom/contact.html'
    success_url = reverse_lazy('classroom:home')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class TeacherCreateView(CreateView):
    # model_form.html
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:home')


class TeacherListView(ListView):
    # model_list.html
    model = Teacher
    # si no se asigna la variable context_object_name entonces la lista se llamará por defecto object_list
    context_object_name = 'teacher_list'
    # si no se asigna la variable queryset entonces retornará por defecto todos los elementos del modelo
    queryset = Teacher.objects.order_by('first_name')


class TeacherDetailView(DetailView):
    # model_detail.html
    model = Teacher


class TeacherUpdateView(UpdateView):
    # model_form.html
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')


class TeacherDeleteView(DeleteView):
    # model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')
