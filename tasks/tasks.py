from celery import shared_task
from django.core.mail import send_mail

from task_manager import env_vars
from tasks.services.mail_service import mail_send

@shared_task
def send_task_mail_notifiaction(subject: str, message: str, recipient: str) -> None:
    print('Sending email')
    print(f'Subject: {subject}')
    print(f'Message: {message}')
    print(f'Recipient: {recipient}')
    send_mail(
        subject,
        message,
        from_email="noreplay@taskmanager.com",
        recipient_list=[recipient],
        fail_silently=False,
    )
    if env_vars.MAILERSEND_API_KEY is not None:
        mail_send(subject=subject, message=message, recipient=recipient)
