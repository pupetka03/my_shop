from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from store.models import Mobile



class ManagerAccessMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()


class ManagerIndex(LoginRequiredMixin, ManagerAccessMixin, ListView):
    template_name = 'manager_index.html'
    login_url = '/login/'
    model = Mobile
    context_object_name = 'mobiles'
