from django import forms
from .models import Review, Booking, Services
class ReviewForm(forms.ModelForm):
    """A form to add a review"""

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


        if user:
            self.fields['fecha_de_la_sesión'].queryset = Booking.objects.filter(user=user)
            
    
        # Exclude author field manually
        self.fields.pop('autor', None)

    def clean_author(self):
        author = self.cleaned_data.get('autor')
        if not author:
            raise forms.ValidationError("Autor es requerido.")
        return author

    class Meta:
        model = Review
        fields = ['fecha_de_la_sesión', 'servicio', 'clasificación', 'texto']