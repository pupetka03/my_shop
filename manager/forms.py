from django import forms
from checkout_app.models import Purchased

class CheckoutManagerForm(forms.ModelForm):
    class Meta:
        model = Purchased
        fields = ['user', 'processed', ]
