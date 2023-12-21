from django.urls import path, include
from .views import main

app_name = 'store'

urlpatterns = [
    path('', main, name='home'),
]
