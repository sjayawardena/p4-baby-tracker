from django.contrib import admin
from .models import NappyChange

# Register your models here.


@admin.register(NappyChange)
class NappyChangeAdmin(admin.ModelAdmin):
    list_display = ("user", "date_and_time", "nappy_contents", "rash", "notes")
    list_filter = ("user", "date_and_time", "nappy_contents", "rash", "notes")
