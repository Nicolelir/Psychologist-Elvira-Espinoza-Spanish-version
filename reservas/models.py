from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from services.models import Services

# Create your models here.
SERVICES_TYPES = (
    ("consulta en línea personalizada", "Consulta en Línea Personalizada"),
    ("terapia individual y familiar en línea", "Terapia individual y Familiar en Línea"),
    ("talleres y grupos de apoyo en línea y presencial", "Talleres y Grupos de Apoyo en Línea y Presencial")
)

TIME_CHOICES = []
start_time = datetime.strptime("09:00", "%H:%M")
end_time = datetime.strptime("18:00", "%H:%M")

while start_time < end_time:
    time_slot = start_time.strftime("%H:%M") + " - " + (start_time + timedelta(hours=1)).strftime("%H:%M")
    TIME_CHOICES.append((time_slot, time_slot))
    start_time += timedelta(hours=1)


class Reserva(models.Model):
    """ A model for booking an appointment """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    servicio = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="reserva", default=1)
    fecha = models.DateField(default=datetime.now, blank=True)
    hora = models.CharField(max_length=20, choices=TIME_CHOICES, default="09:00 - 10:00")
    comentarios = models.TextField(blank=True)

    class Meta:
        """ Order bookings by date """
        ordering = ["-fecha"]
        unique_together = ['fecha', 'hora']

    def __str__(self):
        return f"{self.user.username} - {self.fecha} - {self.hora}"