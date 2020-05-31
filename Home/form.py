from django import forms

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first = forms.CharField(max_length=100)
    last = forms.CharField(max_length=100)
    last = forms.CharField(max_length=10)
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'password', 'first', 'last', 'email', 'phone']
