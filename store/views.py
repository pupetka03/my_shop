from django.shortcuts import render
from .models import Mobile, MobileCategory

# Create your views here.
def main(request):
    category = MobileCategory.objects.filter(is_visible=True)
    return render(request, 'store_main.html')