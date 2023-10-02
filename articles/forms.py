from django import forms
from .models import *

class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'slug', 'thumb']

class EditArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'slug', 'thumb']

