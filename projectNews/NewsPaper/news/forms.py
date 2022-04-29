from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class NewForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'author',
           'title',
           'postCategory',
           'content',
           'rating',
       ]

