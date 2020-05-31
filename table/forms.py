from django import forms
from django.contrib.auth.models import User

from .models import Table, Parameter


class TableForm(forms.ModelForm):

    class Meta:
        model = Table
        fields = ['title']


class ParameterForm(forms.ModelForm):

    class Meta:
        model = Parameter
        fields = ['parameter_title', 'unit']


