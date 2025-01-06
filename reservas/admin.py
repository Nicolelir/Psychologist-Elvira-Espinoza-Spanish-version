from django.contrib import admin
from .models import Reserva

# Register your models here.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'nombre', 'apellido', 'email', 'servicio','fecha', 'hora']