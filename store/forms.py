from django import forms
from .models import EmailSubscriber

class EmailSubscriberForm(forms.ModelForm):
    class Meta:
        model = EmailSubscriber
        fields = ['email']

    email = forms.EmailField(
        label='Your email address here',
        widget=forms.EmailInput(attrs={'placeholder': 'Your email address here', 'required': True, 'size': 60}),
    )
