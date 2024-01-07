from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from store.models import Mobile

# Create your views here.
class ManagerIndex(LoginRequiredMixin, ListView):
    template_name = 'manager_index.html'
    login_url = '/login/'
    model = Mobile
    context_object_name = 'mobiles'
