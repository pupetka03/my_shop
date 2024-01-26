from django.urls import path
from .views import MyAccountView, MyPurchases

urlpatterns = [
    path('account/', MyAccountView.as_view(), name='account'),
    path('account/mypurchases', MyPurchases.as_view(), name='mypurchases'),



]
