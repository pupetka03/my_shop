from django.shortcuts import render, get_object_or_404
from store.models import Mobile, AppleWatch, Banner

def order_mobile(request, mobile_name):
    mobile = get_object_or_404(Mobile, slug=mobile_name)
    banners = Banner.objects.filter(is_visible=True)
    return render(request, 'order_mobile.html', {'mobile': mobile, 'banners': banners})


def order_watch(request, watch_name):
    watch = get_object_or_404(AppleWatch, slug=watch_name)
    return render(request, 'order_watch.html', {'watch': watch})
