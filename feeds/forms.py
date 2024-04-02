from django import forms
from django.forms import ModelForm
from django.forms import DateTimeInput

from .models import Feed


class DateTimeInput(forms.DateTimeInput):
    # input_type = 'date', 'time'
    input_type = "datetime-local"

    # def __init__(self, **kwargs):
    #     kwargs["format"] = '%Y-%m-%dT%H:%M'  # Adjust this format as needed
    #     super().__init__(**kwargs)


class FeedForm(ModelForm):
    """Form to add a nappy change entry"""

    class Meta:
        model = Feed
        fields = [
            "date_and_time",
            "feed_type",
            "formula_amount_ml",
            "breast_feed_time_minutes",
            "notes",
        ]

        widgets = {
            "date_and_time": DateTimeInput(),
        }

        labels = {
            "date_and_time": "Date and Time",
            "feed_type": "Feed Type",
            "formula_amount_ml": "Formula Amount (ml)",
            "breast_feed_time_minutes": "Breast Feed Duration (Minutes)",
            "notes": "Notes",
        }
