from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
"""
Stores a single blog post entry related to :model:`auth.User`.
"""
class Post(models.Model):
     title = models.CharField(max_length=200, unique=True)
     slug = models.SlugField(max_length=200, unique=True)
     content = models.TextField()
     featured_image = CloudinaryField('image', default='placeholder')
     created_on = models.DateTimeField(auto_now_add=True)
     excerpt = models.TextField(blank=True)
     status = models.IntegerField(choices=STATUS, default=0)
     updated_on = models.DateTimeField(auto_now=True)

     class Meta:
        ordering = ["-created_on"]

     def __str__(self):
        return f"{self.title}"