from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_email_function(fname, email, body, lname=None, company=None):
    context = {
        'fname': fname,
        'lname': lname,
        'company': company,
        'email': email,
        'body': body
    }
    email_subject = 'Thank you for your message.'
    email_body = render_to_string('contactforms/email_message.txt', context)
    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email, ],
    )
    return email.send(fail_silently=False)


def send_own_email_function(fname, email, body, lname=None, company=None):
    context = {
        'fname': fname,
        'lname': lname,
        'company': company,
        'email': email,
        'body': body
    }
    email_subject = 'New message.'
    email_body = render_to_string('contactforms/own_email_message.txt', context)
    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, ['nicksportfoliocontact@gmail.com', ],
    )
    return email.send(fail_silently=False)