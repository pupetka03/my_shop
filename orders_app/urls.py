from django.urls import path, include
from .views import order_mobile, order_watch

urlpatterns = [
    path('iphone/<slug:mobile_name>/', order_mobile, name='order_mobile'),
    path('watch/<slug:watch_name>/', order_watch, name='order_watch'),
]
