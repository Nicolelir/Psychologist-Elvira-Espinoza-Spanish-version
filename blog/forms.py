from django import forms
from .models import Post

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'blog_imagen': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }