from django.urls import path
from .views import contacto_form_view, inicio_view

app_name = 'inicio'

urlpatterns = [
    path('', inicio_view, name='inicio'),    
   
]