from django.urls import path
from .views import ManagerIndex, EditCheckout, ConfirmedOrders, search_order

app_name = 'manager'

urlpatterns = [
    path('', ManagerIndex.as_view(), name='index'),
    path('checkouts/<int:pk>', EditCheckout.as_view(), name='edit_checkout'),
    path('confirmed_orders/', ConfirmedOrders.as_view(), name='confirmed_orders'),
    path('search_order/', search_order, name='search_order'),

]