import os
from mailersend import emails

from task_manager import env_vars

# Inicializa el cliente con tu API Key de MailerSend
mailer = emails.NewEmail(env_vars.MAILERSEND_API_KEY)

# Define los parámetros del correo
def mail_send(subject: str, message: str, recipient: str) -> None:
    email_data = {
        'from': {
            'email': 'taskmanager@trial-351ndgw2kvqgzqx8.mlsender.net',
            'name': 'Task Manager'
        },
        'to': [
            {
                'email': recipient,
            }
        ],
        'subject': subject,
        'text': message
        }

    response = mailer.send(email_data)
    print(response)
