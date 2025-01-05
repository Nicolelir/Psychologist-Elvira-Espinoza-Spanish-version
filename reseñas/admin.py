from django.contrib import admin
from .models import Reseña

# Register your models here.
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ['autor', 'creado_el', 'texto']
    ordering = ['-creado_el']

admin.site.register(Reseña, ReseñaAdmin)