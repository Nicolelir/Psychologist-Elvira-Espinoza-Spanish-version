from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking
from datetime import datetime, timedelta

class BookingForm(forms.ModelForm):
    """A form to add a booking"""

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
          self.fields['email'].initial = user.email
        self.fields['nombre'].required = True
        self.fields['apellido'].required = True
        self.fields['servicio'].required = True
        self.fields['fecha'].required = True

        self.fields['nombre'].label = "Nombre"
        self.fields['apellido'].label = "Apellido"
        self.fields['servicio'].label = "Servicio"
        self.fields['fecha'].widget = forms.DateInput(attrs={'type': 'date'})

    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        hora = cleaned_data.get('hora')

        # Check if a booking with the same date and time already exists
        if (fecha and hora and
                Booking.objects.filter(fecha=fecha, hora=hora).exists()):
            self.add_error('hora', 'Esta fecha y hora ya ha sido seleccionada, por favor escoge otra')

    class Meta:
        model = Booking
        fields = [
            'nombre', 'apellido', 'email', 'servicio', 'fecha', 'hora'
        ]

    