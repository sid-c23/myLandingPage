from django.shortcuts import render, redirect
from .forms import SendEmailForm
from django.core.mail import EmailMessage
# Create your views here.
def emailHome(request):

    if request.user.is_authenticated():
        form = SendEmailForm(request.POST or None)

        if form.is_valid():
            email_sub = form.cleaned_data.get('email_subject')
            email_body = form.cleaned_data.get('email_body')
            email_from = ''#form.cleaned_data.get('email_from')
            email_to = list(form.cleaned_data.get('email_to').values_list('email', flat=True))
            email = EmailMessage(
            email_sub,
            email_body,
            email_from,
            email_to,
            ['chagantisidhartha@gmail.com'],
            )
            email.send(fail_silently=False)



        context = {
            'form': form
        }
    else:
        return redirect('HomeSignUp:landing')

    return render(request, 'sendEmail.html', context)