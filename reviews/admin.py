from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['autor', 'creado_el', 'texto']
    ordering = ['-creado_el']

admin.site.register(Review, ReviewAdmin)