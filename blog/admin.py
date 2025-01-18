from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from .forms import PostAdminForm

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    form = PostAdminForm
    
    list_display = ('título', 'slug', 'estado', 'creado_en')
    search_fields = ['título', 'contenido']
    list_filter = ('estado', 'creado_en',)
    prepopulated_fields = {'slug': ('título',)}
    summernote_fields = ('contenido',)

# Register your models here.
