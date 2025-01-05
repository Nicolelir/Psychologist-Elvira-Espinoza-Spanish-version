from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReseñaPagina.as_view(), name='reseñas'),
    path('agrega/', views.AgregaReseña.as_view(), name='reseña_agrega'),
    path('reseña/<int:pk>/', views.ReseñaDetalle.as_view(), name='reseña_detalle'),

    
]