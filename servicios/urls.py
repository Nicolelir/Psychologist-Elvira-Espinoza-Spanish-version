from django.urls import path
from . import views
from .views import ServiciosListView

urlpatterns = [
path('', ServiciosListView.as_view(), name='servicios'),

]