from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'consulta']