from celery import shared_task
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError

from .models import Mailing, Message, MailingLog, Client


@shared_task
def send_messages():
    mailings = Mailing.objects.filter(status="CREATED")

    for mailing in mailings:
        if mailing.start_time <= datetime.now() and (not mailing.end_time or mailing.end_time >= datetime.now()):
            messages = Message.objects.filter(mailing=mailing)

            for message in messages:
                for client in Client.objects.all():
                    try:
                        # Отправка сообщения
                        send_mail(
                            subject=message.subject,
                            message=message.body,
                            from_email='irinka_p08@mail.ru',  # Замените на ваш адрес отправителя
                            recipient_list=[client.email],
                            fail_silently=False,
                        )
                        log_status = "SUCCESS"
                    except (BadHeaderError, Exception) as e:
                        # Если произошла ошибка при отправке
                        log_status = "FAILED"

                    log = MailingLog(message=message, client=client, status=log_status, response=str(e) if log_status == "FAILED" else "Message sent successfully")
                    log.save()

            mailing.status = "COMPLETED"
            mailing.save()
