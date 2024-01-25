from django import forms
from .models import Purchased

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Purchased
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'country', 'zip_code', 'telephone']