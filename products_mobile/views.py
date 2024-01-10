from django.shortcuts import render
from store.models import MobileCategory, Banner


def products(request):
    categories = MobileCategory.objects.filter(is_visible=True)
    banners = Banner.objects.filter(is_visible=True)
    return render(request, 'products_mobile.html', {'categories': categories, 'banners': banners})

