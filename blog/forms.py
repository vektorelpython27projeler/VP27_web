from django import forms
from .models import BlogModel
class BlogForm(forms.ModelForm):

    class Meta:
        model=BlogModel
        fields = ('baslik','yazi','tur')