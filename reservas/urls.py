from django.urls import path
from . import views


urlpatterns = [
    path("", views.ReservasPagina.as_view(), name='reservas'),
    path('agrega/', views.AgregaReserva.as_view(), name='reserva_agrega'),
    path('edita/<int:pk>/', views.EditaReserva.as_view(), name='edita_reserva'),
    path('elimina/<int:pk>/',views.EliminaReserva.as_view(), name='elimina_reserva'),
     path('horas_disponibles/', views.horas_disponibles, name='horas_disponibles'),
    
]