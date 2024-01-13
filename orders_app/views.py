from django.shortcuts import render, get_object_or_404
from store.models import Mobile, MobileCategory, Banner

def order(request, mobile_name):
    mobile = get_object_or_404(Mobile, slug=mobile_name)
    banners = Banner.objects.filter(is_visible=True)
    return render(request, 'order.html', {'mobile': mobile, 'banners': banners})
