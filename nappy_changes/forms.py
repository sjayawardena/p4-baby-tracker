from django import forms
from django.forms import ModelForm

from .models import NappyChange

class DateTimeInput (forms.DateTimeInput):
    input_type = 'date', 'time'
    
class NappyChangeForm(ModelForm):
    
    class Meta: 
        model = NappyChange
        fields = ['user', 'date_and_time', 'nappy_contents', 'rash', 'notes']
        widgets = {
            'date_and_time': DateTimeInput(),
        }