__author__ = 'chaga'
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'email',
            'name',
            'message'
        ]