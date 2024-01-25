from django.urls import path
from .views import ManagerIndex, EditCheckout

app_name = 'manager'

urlpatterns = [
    path('', ManagerIndex.as_view(), name='index'),
    path('checkouts/<int:pk>', EditCheckout.as_view(), name='edit_checkout'),
]