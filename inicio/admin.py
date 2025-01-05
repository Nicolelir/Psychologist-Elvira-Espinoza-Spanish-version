from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contacto



# Register your models here.

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):

    list_display = ('consulta', 'fecha','leido',)