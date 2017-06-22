from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.
def contact(request):
    request_post = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        form_email = form.cleaned_data.get('email')
        form_name = form.cleaned_data.get('name')
        form_message = form.cleaned_data.get('message')

        subject = 'Someone Contacted Us!'
        contactMessage = """
        %s at %s: %s
        """%(form_name, form_email, form_message)
        fromEmail = settings.EMAIL_HOST_USER
        toEmail = [fromEmail, 'chagantisidhartha@gmail.com']
        send_mail(subject, contactMessage, fromEmail, toEmail, fail_silently=False)
        instance.save()
    if request.method == 'POST':
        request_post = True
    context = {
        "form":form,
        'submitted':request_post
    }
    return render(request, 'contact.html', context)