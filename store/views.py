from django.shortcuts import render, redirect
from .models import Mobile, MobileCategory, Banner, BannerPromo, AppleWatch, WatchCategory
from .forms import EmailSubscriberForm
from django.views.generic import TemplateView
from django.contrib import messages

# def main(request):
#     categories  = MobileCategory.objects.filter(is_visible=True)

#     context = {
#         'categories': categories,
               
#     }

#     return render(request, 'store_main.html', context=context) 


class IndexPage(TemplateView):
    template_name = "store_main.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['categories'] = MobileCategory.objects.filter(is_visible=True)
        context['watch_categories'] = WatchCategory.objects.filter(is_visible=True)
        context['form_emails'] = EmailSubscriberForm
        context['banners'] = Banner.objects.filter(is_visible=True)
        context['bannerpromos'] = BannerPromo.objects.filter(is_visible=True)
        return context
    

    def post(self, request, *args, **kwargs):
        form_emails = EmailSubscriberForm(request.POST)

        if form_emails.is_valid():
            form_emails.save()
            messages.success(self.request, 'subscribe done')
            return redirect('/')
        
        context = self.get_context_data()
        context['form_emails'] = EmailSubscriberForm
        messages.error(self.request, 'Errors in form form_emails')
        return render(self.request, self.template_name, context=context)
            

    
