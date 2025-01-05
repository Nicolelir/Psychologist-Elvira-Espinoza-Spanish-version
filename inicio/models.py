from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.
home_image = CloudinaryField('image', default='placeholder')

class Contacto(models.Model):
    """
    Stores a single contact form message
    """
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    consulta = models.TextField()
    fecha = models.DateField(default=datetime.now, blank=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact form {self.nombre}"
