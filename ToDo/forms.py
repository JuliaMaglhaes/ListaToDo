from django import forms
from django.forms import ModelForm
from .models import *

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = '__all__'