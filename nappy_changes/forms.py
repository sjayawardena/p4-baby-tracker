from django import forms
from django.forms import ModelForm
from django.forms import DateTimeInput

from .models import NappyChange


class DateTimeInput(forms.DateTimeInput):
    # input_type = 'date', 'time'
    input_type = "datetime-local"

    # def __init__(self, **kwargs):
    #     kwargs["format"] = '%Y-%m-%dT%H:%M'  # Adjust this format as needed
    #     super().__init__(**kwargs)


class NappyChangeForm(ModelForm):
    """Form to add a nappy change entry"""

    class Meta:
        model = NappyChange
        fields = ["date_and_time", "nappy_contents", "rash", "notes"]

        widgets = {
            "date_and_time": DateTimeInput(),
        }

        labels = {
            "date_and_time": "Date and Time",
            "nappy_contents": "Nappy Contents",
            "rash": "Rash",
            "notes": "Notes",
        }
