from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import SignUpForm
import os
# Create your views here.
def landing(request):
    post_request = False
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        formName = form.cleaned_data.get('first_name')
        formEmail = form.cleaned_data.get('email')
        fromEmail = settings.EMAIL_HOST_USER
        toEmail = [formEmail]
        subjectMessage = 'Hello %s, here is your PDF!'%(formName)
        sendPDFMessage = """
        Hello, %s,
        Thank you for signing up to our email list. We will make sure to send you worthwhile emails.

        In the mean time, here is your PDF!

        Enjoy,
        %s
        """%(formName, fromEmail)
        attachedFile = os.path.join(os.path.join(settings.BASE_DIR, 'attachments'), 'hello.txt')
        email = EmailMessage(
        subjectMessage,
        sendPDFMessage,
        fromEmail,
        toEmail,
        ['chagantisidhartha@gmail.com'],
        )
        email.attach_file(attachedFile)
        email.send(fail_silently=False)
        instance.save()
    if request.method == 'POST':
        post_request = True

    context = {
            'form':form,
            'submitted': post_request
        }
    return render(request, 'home.html', context)