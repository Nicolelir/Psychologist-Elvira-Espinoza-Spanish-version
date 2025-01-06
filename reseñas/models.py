from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField
from reservas.models import Reserva
from services. models import Services


class Reseña(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reseñas")
    servicio = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="reseñas",  default=1)
    fecha_de_la_sesión =  models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="reserva",  default=1)
    creado_el = models.DateTimeField(default=datetime.now)
    clasificación = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1)
    texto = models.TextField()

    class Meta:
        ordering = ['-creado_el']

    def __str__(self):
        return f"Review by {self.autor.username} on {self.creado_el}"

     # Methods to calculate full and empty stars
    def full_stars(self):
        """Returns a range object representing filled stars."""
        return range(self.clasificación)

    def empty_stars(self):
        """Returns a range object representing unfilled stars."""
        return range(5 - self.clasificación)   