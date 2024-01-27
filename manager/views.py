import uuid
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, FormView
from store.models import Mobile
from checkout_app.models import Purchased
from manager.forms import CheckoutManagerForm, OrderSearchForm
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
        context['orders'] = Purchased.objects.filter(processed=False)
        context['cart_items'] = CartItem.objects.all
        return context
    

class EditCheckout(LoginRequiredMixin, ManagerAccessMixin, UpdateView):
    template_name = 'edit_checkouts.html'
    model = Purchased
    login_url = '/login/'
    form_class = CheckoutManagerForm
    success_url = reverse_lazy('manager:index')
    
    
class ConfirmedOrders(LoginRequiredMixin, ManagerAccessMixin, ListView):
    template_name = 'confirmed_orders.html'
    login_url = '/login/'
    model = Purchased
    context_object_name = 'confirmed_orders'

    def get_queryset(self):
        return Purchased.objects.filter(processed=True)




def search_order(request):
    form = OrderSearchForm(request.GET)
    orders = []

    if form.is_valid():
        order_code = form.cleaned_data['order_code']

        try:
            uuid.UUID(order_code, version=4)
        except ValueError:
            form.add_error('order_code', 'The order number format is incorrect')
            return render(request, 'search_order.html', {'form': form, 'orders': orders})

        orders = Purchased.objects.filter(order_code__endswith=order_code)


        
    return render(request, 'search_order.html', {'form': form, 'orders': orders})


    
