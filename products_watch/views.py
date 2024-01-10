from django.shortcuts import render
from store.models import WatchCategory, Banner


def products(request):
    watch_categories = WatchCategory.objects.filter(is_visible=True)
    banners = Banner.objects.filter(is_visible=True)
    return render(request, 'products_watch.html', {'watch_categories': watch_categories, 'banners': banners})

