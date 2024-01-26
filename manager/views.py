from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, FormView
from store.models import Mobile
from checkout_app.models import Purchased
from manager.forms import CheckoutManagerForm
from django.shortcuts import render
from checkout_app.models import Purchased
from checkout_app.views import CartItem
from django.urls import reverse_lazy

class ManagerAccessMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()


class ManagerIndex(LoginRequiredMixin, ManagerAccessMixin, ListView):
    template_name = 'manager_index.html'
    login_url = '/login/'
    model = Mobile
    context_object_name = 'mobiles'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Purchased.objects.all()
        context['cart_items'] = CartItem.objects.all
        return context
    

class EditCheckout(LoginRequiredMixin, ManagerAccessMixin, UpdateView):
    template_name = 'edit_checkouts.html'
    login_url = '/login/'
    form_class = CheckoutManagerForm
    success_url = reverse_lazy('manager:index')
    model = Purchased
    




    
