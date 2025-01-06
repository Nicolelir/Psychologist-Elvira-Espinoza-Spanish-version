from django.db import models
from djrichtextfield.models import RichTextField
from cloudinary.models import CloudinaryField



# Create your models here.


class Servicios(models.Model):
    título = models.CharField(max_length=200)
    descripción = RichTextField(max_length=10000, null=False, blank=False)
    imagen = CloudinaryField('imagen', default='placeholder')

    def __str__(self):
        return self.título