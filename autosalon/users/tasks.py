from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_confirmation_email(email: str):
    subject = 'Confirmation Email'
    message = 'Please confirm your email'
    from_email = "mariam.frami@ethereal.email"
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)