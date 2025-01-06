from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Reserva
from datetime import datetime, timedelta

class ReservaForm(forms.ModelForm):
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

      # Restrict fecha to future dates
        self.fields['fecha'].widget = forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()})
        
        # Dynamically limit hora choices if fecha is selected
        self.fields['hora'].choices = self.get_horas_disponibles()

    def get_horas_disponibles(self):
        """
        Returns a list of available time slots based on the selected date.
        """
        fecha = self.data.get('fecha')  # Retrieve selected fecha from form data
        if not fecha:
            # Default to all slots if no date is selected yet
            return [
                ('09:00 - 10:00', '09:00 - 10:00'),
                ('10:00 - 11:00', '10:00 - 11:00'),
                ('11:00 - 12:00', '11:00 - 12:00'),
                ('12:00 - 13:00', '12:00 - 13:00'),
                ('14:00 - 15:00', '14:00 - 15:00'),
                ('15:00 - 16:00', '15:00 - 16:00'),
                ('16:00 - 17:00', '16:00 - 17:00'),
                ('17:00 - 18:00', '17:00 - 18:00')
            ]
        
        # Parse fecha and filter existing bookings
        selected_date = datetime.strptime(fecha, '%Y-%m-%d').date()
        booked_slots = Reserva.objects.filter(fecha=selected_date).values_list('hora', flat=True)
        
        # Define all possible time slots
        todas_horas_disponibles = [
            '09:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00',
            '12:00 - 13:00', '14:00 - 15:00',
            '15:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00'
        ]
        
        # Filter out booked slots
        horas_disponibles = [(slot, slot) for slot in all_time_slots if slot not in booked_slots]
        
        return horas_disponibles

    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        hora = cleaned_data.get('hora')

        # Check if a booking with the same date and time already exists
        if (fecha and hora and
                Reserva.objects.filter(fecha=fecha, hora=hora).exists()):
            self.add_error('hora', 'Esta fecha y hora ya ha sido seleccionada, por favor escoge otra')

    class Meta:
        model = Reserva
        fields = [
            'nombre', 'apellido', 'email', 'servicio', 'fecha', 'hora'
        ]

    