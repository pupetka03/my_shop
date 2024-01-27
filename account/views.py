from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, UserLoginForm
from django.views.generic import TemplateView
from checkout_app.models import Purchased


# User Logout
def logout_user(request):
    logout(request)
    return redirect('store:home')

# User Regastrations
class RegisterUser(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

# User Login
class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return self.request.GET.get('next') or self.request.POST.get('next') or '/'
    

#account
class MyAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'account.html'
    
    def get(self, request, *args, **kwargs):
        context = {
            'username': request.user.username,
            'email': request.user.email,
        }
        return render(request, self.template_name, context)
    
#account purchases
class MyPurchases(LoginRequiredMixin, TemplateView):
    template_name = 'my_purchases.html'
    
    def get(self, request):
        orders = Purchased.objects.filter(user=request.user)
        context = {'orders': orders}
        return render(request, self.template_name, context)