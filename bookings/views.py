from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Booking
from .forms import BookingForm



class BookingsPage(ListView):
    """View for displaying bookings"""
    model = Booking
    template_name = 'bookings/bookings.html'  
    context_object_name = 'bookings' 

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'bookings': bookings})

# LoginRequiredMixin: only authenticated users can access a particular view. If a user is not authenticated, they will be redirected to the login page.
class AddBooking(LoginRequiredMixin, CreateView): 
    """Add booking view"""

    template_name = "bookings/add_booking.html"
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy("bookings")

    def form_valid(self, form):
        # Set the current user as the booking user
        form.instance.user = self.request.user
        selected_date = form.cleaned_data.get('fecha')
        selected_time_str = form.cleaned_data.get('hora')

        # Get the current date and time
        current_datetime = timezone.now()

       # Check if date is in the past
        selected_time = datetime.strptime(selected_time_str.split(' - ')[0], '%H:%M').time()
        if (selected_date < current_datetime.date() or
            (selected_date == current_datetime.date() and
             selected_time < current_datetime.time())):
            form.add_error('fecha', 'Por favor ingrese una fecha válida')
            return self.form_invalid(form)

        messages.success(self.request, "¡Gracias por agendar una hora conmigo! No olvides dejar una reseña después de tu sesión.")
        return super().form_valid(form)

# UserPassesTestMixin:This mixin allows to define custom permission checks for a view. 
class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/edit_booking.html'
    success_url = reverse_lazy('bookings')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def form_valid(self, form):
        form.instance.user = self.request.user

         # Exclude date and time fields from cleaned data - credit Django docs
        cleaned_data = form.cleaned_data
        new_date = cleaned_data.get('date')
        new_time = cleaned_data.get('time')

        # Check if the new time and date are available
        if new_date and new_time:
            existing_booking = Booking.objects.filter(
                date=new_date,
                time=new_time).exclude(pk=self.object.pk).first()
            if existing_booking:
                form.add_error('time', 'Esta fecha y hora ya estan tomadas, por favor escoge otra')
                return self.form_invalid(form)

        messages.success(self.request, "Tu reserva ha sido actualizada.")

        return super().form_valid(form)

class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a  Booking
    """
    model = Booking
    template_name = 'bookings/delete_booking.html'
    success_url = reverse_lazy('bookings')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def delete(self, request, *args, **kwargs):
        # Display success message
        messages.success(self.request, "Tu reserva ha sido eliminada.")

        return super().delete(request, *args, **kwargs)
