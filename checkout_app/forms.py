# forms.py
from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address', widget=forms.Textarea)
    city = forms.CharField(label='City', max_length=100)
    country = forms.CharField(label='Country', max_length=100)
    zip_code = forms.CharField(label='ZIP Code', max_length=10)
    telephone = forms.CharField(label='Telephone', max_length=15)
