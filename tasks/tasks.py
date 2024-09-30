from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_task_mail_notifiaction(subject: str, message: str, recipient: list[str]) -> None:
    print('Sending email')
    print(f'Subject: {subject}')
    print(f'Message: {message}')
    print(f'Recipient: {recipient}')
    send_mail(
        subject,
        message,
        from_email="angel.de.oz.97@gmail.com",
        recipient_list=recipient,
        fail_silently=False,
    )
