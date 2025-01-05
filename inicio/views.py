from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm 
from .models import Contacto

def contacto_form_view(request):
    message_sent = False  # Initialize the success message flag
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            # Set the success message flag to True
            message_sent = True
    else:
        form = ContactoForm() 

    return render(request, 'inicio/index.html', {'form': form, 'message_sent': message_sent})

def inicio_view(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu mensaje ha sido enviado con éxito!")
            return redirect('inicio:inicio')  # Redirect to the home page to clear the form
    else:
        form = ContactoForm()

    return render(request, 'inicio/index.html', {'form': form})

   