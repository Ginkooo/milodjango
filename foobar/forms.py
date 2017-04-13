from django import forms
from django.conf import settings
from foobar.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    birthday = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = User
        fields = ['birthday', 'username', 'password', 'email', 'number']
        help_texts = {
                'email': 'Format: month-day-year (eg. 12-09-1995)',
                }
