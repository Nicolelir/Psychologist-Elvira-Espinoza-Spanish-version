from django.contrib import admin
from .models import Servicios


# Register your models here.
@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
   list_display = ('título', 'descripción')
   