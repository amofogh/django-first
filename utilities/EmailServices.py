from p import settings
from django.core.mail import send_mail


def send_email(subject, message, to: list):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, to)
