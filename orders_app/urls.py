from django.urls import path, include
from .views import order

urlpatterns = [
    path('<slug:mobile_name>/', order, name='order'),

]
