from django.contrib import admin
from .models import NappyChange, Feed

# Register your models here.

@admin.register(NappyChange)
class NappyChangeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date_and_time',
        'nappy_contents',
        'rash',
        'notes'
    )
    list_filter = ('user', 'date_and_time', 'nappy_contents', 'rash','notes')
    
    
@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = (
    'user',
    'date_and_time',
    'feed_type',
    'formula_amount_ml',
    'breast_feed_time_minutes',
    'notes'
    )
    list_filter = ('user', 'date_and_time', 'feed_type', 'formula_amount_ml',
                   'breast_feed_time_minutes', 'notes')