from django.urls import path
from .views import AddNappyChange


urlpatterns = [
    path('', AddNappyChange.as_view(), name = 'add_nappy_change'),
]