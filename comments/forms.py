from django import forms
from comments import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name','email', 'url', 'text']
