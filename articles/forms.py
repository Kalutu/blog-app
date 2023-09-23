from django import forms
from .models import *

class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'body', 'thumb']
