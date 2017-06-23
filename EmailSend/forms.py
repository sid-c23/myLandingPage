__author__ = 'chaga'
from django import forms
from HomeSignUp.models import SignUp


class SendEmailForm(forms.Form):
    email_subject = forms.CharField(max_length=80, label='Subject')
    email_body = forms.CharField(widget=forms.Textarea(), label='Body')
    # email_from = forms.EmailField(label='From (your gmail address. Impersonation is looked down upon!)')
    email_to = forms.ModelMultipleChoiceField(
        label='Emails',
        queryset=SignUp.objects.all(),
        required=True
    )
