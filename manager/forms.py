from django import forms
from checkout_app.models import Purchased

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Purchased
        fields = ['processed']

