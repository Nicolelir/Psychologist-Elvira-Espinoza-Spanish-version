"""
URL configuration for Elvira_bookings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LogoutView
from django.contrib.auth.views import LoginView

from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path("servicios/", include("servicios.urls")),
    path('reservas/', include('reservas.urls')),
    path("reseñas/", include("reseñas.urls")),
    path("blog/", include("blog.urls")),
    path('accounts/', include('allauth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('summernote/', include('django_summernote.urls')),

    path('cuenta/registrarse/', RedirectView.as_view(pattern_name='account_signup'), name='cuenta_registrarse'),
    path('cuentas/iniciar-sesion/', LoginView.as_view(), name='cuenta_iniciar_sesion'),
    path('cuenta/cerrar-sesion/', LogoutView.as_view(), name='cuenta_cerrar_sesion'),
    
]
