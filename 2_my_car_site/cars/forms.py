from django import forms
from .models import Review
from django.forms import ModelForm

# crear forms de forma manual
# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First name', max_length=100)
#     last_name = forms.CharField(label='Last name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here', widget=forms.Textarea(attrs={'class':'myform'}))

#crear forms a partir de modelos
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # se especifican los campos con una lista en la variable fields, o se pasan todos con __all__, o se pueden excluir algunos con la variable exclude
        fields = '__all__'
        labels = {
            'first_name': "Your first name",
            'last_name': "Your last name",
            'stars': 'Rating'
        }

        error_messages = {
            'stars': {
                'min_value': 'Min value is 1',
                'max_value': 'Max value is 5'
            }
        }