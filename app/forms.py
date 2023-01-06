from django import forms
from .models import Guardias, Empresa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GuardiaForm(forms.ModelForm):
    
    class Meta:
        model = Guardias
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    pass

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        
