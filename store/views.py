from django.shortcuts import render
from .models import Mobile, MobileCategory

# Create your views here.
def main(request):
    categories  = MobileCategory.objects.filter(is_visible=True)

    context = {
        'categories': categories,
               
    }

    return render(request, 'store_main.html', context=context) 