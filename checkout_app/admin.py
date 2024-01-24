from django.contrib import admin
from .models import Purchased

class PurchasedAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email', 'address', 'city', 'country', 'zip_code', 'telephone', 'processed', 'order_code']

admin.site.register(Purchased, PurchasedAdmin)
