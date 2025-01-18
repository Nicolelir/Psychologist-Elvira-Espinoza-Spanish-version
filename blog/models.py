from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

ESTADO = ((0, "Borrador"), (1, "Publicado"))

def validate_file_size(value):
    max_size = 10 * 1024 * 1024  # 10 MB
    if value.size > max_size:
        raise ValidationError(f"El tamaño del archivo no puede exceder {max_size / (1024 * 1024)} MB.")

# Create your models here.
"""
Stores a single blog post entry related to :model:`auth.User`.
"""
class Post(models.Model):
     título = models.CharField(max_length=200, unique=True)
     slug = models.SlugField(max_length=200, unique=True)
     contenido = models.TextField()
     blog_imagen = CloudinaryField('image', blank=True, null=True)
     video  = models.FileField(upload_to='videos/', blank=True, null=True)
     video_link = models.URLField(max_length=500, blank=True, null=True)
     creado_en = models.DateTimeField(auto_now_add=True)
     extracto = models.TextField(blank=True)
     estado = models.IntegerField(choices=ESTADO, default=0)
     actualizado_en = models.DateTimeField(auto_now=True)

     class Meta:
        ordering = ["-creado_en"]

     def __str__(self):
        return f"{self.título}"