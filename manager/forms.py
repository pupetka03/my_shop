from django import forms
from checkout_app.models import Purchased

class CheckoutManagerForm(forms.ModelForm):
    class Meta:
        model = Purchased
        fields = ['user', 'processed', ]


class OrderSearchForm(forms.Form):
    order_code = forms.CharField(max_length=50, label='Код замовлення', widget=forms.TextInput(attrs={'placeholder': 'Введіть код замовлення'}))
