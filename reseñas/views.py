from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
from .forms import ReseñaForm
from .models import Reseña
from .models import Reserva

class ReseñaPagina(ListView):
    """View for displaying reviews"""
    model = Reseña
    template_name = 'reseñas/reseñas.html'  
    context_object_name = 'reseñas' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for reseña in context['reseñas']:
            reseña.full_stars = range(reseña.clasificación)
            reseña.empty_stars = range(5 - reseña.clasificación)
        return context
        
  
@login_required
def agrega_reseña(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if booking.user != request.user:
        # User is not authorized to leave a review for this booking
        return redirect('inicio')  

    if request.method == 'POST':
        form = ReseñaForm(request.POST, user=request.user)  
        if form.is_valid():
            reseña = form.save(commit=False)
            reseña.booking = booking
            reseña.author = request.user
            reseña.save()
            return redirect('reservas', booking_id=booking_id)  
    else:
        form = ReseñaForm(user=request.user)  
    return render(request, 'agrega_reseña.html', {'form': form})


class AgregaReseña(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    A model to create a review
    """
    template_name = 'reseñas/agrega_reseñas.html'
    model = Reseña
    form_class = ReseñaForm
    success_url = reverse_lazy('reseñas')  
   
    def form_valid(self, form):
        # Set the author of the review to the current user
        form.instance.autor = self.request.user
        # Save the review instance
        response = super().form_valid(form)
        # Display success message
        messages.success(self.request, 'Tu reseña ha sido agregada!')
        return response

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user 
        return kwargs

class ReseñaPagina(ListView):
    """
    A view to display a paginated list of reviews.
    """
    model = Reseña
    template_name = 'reseñas/reseñas.html'
    context_object_name = 'reseñas'
    paginate_by = 6 

class ReseñaDetalle(DetailView):
    """View a single review"""

    template_name = "reseñas/reseña_detalle.html"
    model = Reseña
    context_object_name = "reseña"


   
