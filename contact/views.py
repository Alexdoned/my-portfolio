from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        contact_message = form.save()
        send_mail(
            f'New contact form: {contact_message.subject}',
            f'From: {contact_message.name} <{contact_message.email}>\n\n{contact_message.message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],
            fail_silently=True,
        )
        messages.success(request, 'Thank you! Your message has been sent successfully.')
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form,
    })
