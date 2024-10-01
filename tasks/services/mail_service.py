from mailersend import emails

from task_manager import env_vars
from tasks.types import EmailInfo, MailAction


mailer = emails.NewEmail(env_vars.MAILERSEND_API_KEY)


def create_mail(type: MailAction, task_title: str, task_description: str) -> EmailInfo:
    if type == MailAction.CREATE:
        subject = 'Nueva tarea asignada'
        message = f'''Se ha creado una nueva tarea: {task_title}\n descripcion: {task_description}'''
    elif type == MailAction.UPDATE:
        subject = 'Tarea actualizada'
        message = f'''La tarea: {task_title} ha sido actualizada\n descripcion: {task_description}'''
    
    return {
        'subject': subject,
        'message': message,
    }

def mail_send(subject: str, message: str, email: str) -> None:

    email_data = {
        'from': {
            'email': env_vars.MAILERSEND_EMAIL,
            'name': 'Task Manager'
        },
        'to': [
            {
                'email': email,
            }
        ],
        'subject': subject,
        'text': message
    }


    send = mailer.send(email_data)
    print(send)
