from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class FormHome(forms.Form):
    username = forms.CharField(label=False)


class ProfileCreationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')