from django import forms
from checkout_app.models import Purchased

class CheckoutManagerForm(forms.ModelForm):
    class Meta:
        model = Purchased
        fields = ['user', 'processed', ]


class OrderSearchForm(forms.Form):
    order_code = forms.CharField(max_length=50, label='Order code', widget=forms.TextInput(attrs={'placeholder': 'Enter the order code'}))
