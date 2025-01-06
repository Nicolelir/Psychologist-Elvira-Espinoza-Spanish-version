from django.shortcuts import render
from django.views.generic import ListView
from .models import Servicios



# Create your views here.

class ServiciosListView(ListView):
    """View all services"""

    template_name = "servicios/servicios.html"
    queryset = Servicios.objects.all()
    context_object_name = "servicios"