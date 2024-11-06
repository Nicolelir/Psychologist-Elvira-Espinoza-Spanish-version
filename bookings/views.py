from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import JsonResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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
    """View for displaying a user's bookings"""
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/bookings.html', {'bookings': bookings})

@login_required
def available_slots(request):
    """Return available time slots for a given date."""
    selected_date = request.GET.get('date')
    if selected_date:
        selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
        booked_times = Booking.objects.filter(fecha=selected_date).values_list('hora', flat=True)
        
        all_time_slots = [
            '09:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00',
            '12:00 - 13:00', '14:00 - 15:00',
            '15:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00'
        ]
        
        available_slots = [slot for slot in all_time_slots if slot not in booked_times]
        return JsonResponse({'available_slots': available_slots})

    return JsonResponse({'available_slots': []})

class AddBooking(LoginRequiredMixin, CreateView): 
    """Add booking view"""
    template_name = "bookings/add_booking.html"
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy("bookings")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        selected_date = self.request.POST.get('fecha', None)
        
        if selected_date:
            selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
            booked_times = Booking.objects.filter(fecha=selected_date).values_list('hora', flat=True)
            
            all_time_slots = [
                '09:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00',
                '12:00 - 13:00', '14:00 - 15:00',
                '15:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00'
            ]
            
            available_time_slots = [slot for slot in all_time_slots if slot not in booked_times]
            
            form.fields['hora'].choices = [(slot, slot) for slot in available_time_slots]

        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        selected_date = form.cleaned_data.get('fecha')
        selected_time_str = form.cleaned_data.get('hora')

        current_datetime = timezone.now()
        selected_time = datetime.strptime(selected_time_str.split(' - ')[0], '%H:%M').time()
        
        if (selected_date < current_datetime.date() or
            (selected_date == current_datetime.date() and
             selected_time < current_datetime.time())):
            form.add_error('fecha', 'Por favor ingrese una fecha válida')
            return self.form_invalid(form)

        messages.success(self.request, "¡Gracias por agendar una hora conmigo! No olvides dejar una reseña después de tu sesión.")
        return super().form_valid(form)

class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a booking"""
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/edit_booking.html'
    success_url = reverse_lazy('bookings')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        cleaned_data = form.cleaned_data
        new_date = cleaned_data.get('fecha')
        new_time = cleaned_data.get('hora')

        if new_date and new_time:
            existing_booking = Booking.objects.filter(
                fecha=new_date,
                hora=new_time).exclude(pk=self.object.pk).first()
            if existing_booking:
                form.add_error('hora', 'Esta fecha y hora ya están tomadas, por favor escoge otra')
                return self.form_invalid(form)

        messages.success(self.request, "Tu reserva ha sido actualizada.")
        return super().form_valid(form)

class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a Booking"""
    model = Booking
    template_name = 'bookings/delete_booking.html'
    success_url = reverse_lazy('bookings')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Tu reserva ha sido eliminada.")
        return super().delete(request, *args, **kwargs)