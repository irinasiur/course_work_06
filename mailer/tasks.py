from celery import shared_task
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError

from .models import Mailing, Message, MailingLog, Client
from django.utils import timezone


@shared_task
def send_messages():
    now = datetime.now()
    mailings = Mailing.objects.filter(status="CREATED", start_time__lte=now, end_time__gte=now)

    for mailing in mailings:
        if mailing.start_time <= timezone.now() and (not mailing.end_time or mailing.end_time >= timezone.now()):
            messages = Message.objects.filter(mailing=mailing)

            for message in messages:
                for client in Client.objects.all():
                    log_status = "SUCCESS"
                    response_message = "Message sent successfully"

                    try:
                        send_mail(
                            subject=message.subject,
                            message=message.body,
                            from_email='irinka_p08@mail.ru',  # Замените на ваш адрес отправителя
                            recipient_list=[client.email],
                            fail_silently=False,
                        )
                    except (BadHeaderError, Exception) as e:
                        log_status = "FAILED"
                        response_message = str(e)

                    # Предполагается, что user_id доступен через message.user_id
                    # Если это не так, замените эту строку соответствующим кодом
                    user_id = message.user_id

                    log = MailingLog(
                        message=message,
                        client=client,
                        status=log_status,
                        response=response_message,
                        user_id=user_id  # Передача user_id при создании объекта log
                    )
                    log.save()

            mailing.status = "COMPLETED"
            mailing.save()

#
# @shared_task
# def send_messages():
#     # mailings = Mailing.objects.filter(status="CREATED")
#     now = datetime.now()
#     mailings = Mailing.objects.filter(status="CREATED", start_time__lte=now, end_time__gte=now)
#
#     for mailing in mailings:
#         if mailing.start_time <= timezone.now() and (not mailing.end_time or mailing.end_time >= timezone.now()):
#         # if mailing.start_time <= datetime.now() and (not mailing.end_time or mailing.end_time >= datetime.now()):
#             messages = Message.objects.filter(mailing=mailing)
#
#             for message in messages:
#                 for client in Client.objects.all():
#                     try:
#                         # Отправка сообщения
#                         send_mail(
#                             subject=message.subject,
#                             message=message.body,
#                             from_email='irinka_p08@mail.ru',  # Замените на ваш адрес отправителя
#                             recipient_list=[client.email],
#                             fail_silently=False,
#                         )
#                         log_status = "SUCCESS"
#                     except (BadHeaderError, Exception) as e:
#                         # Если произошла ошибка при отправке
#                         log_status = "FAILED"
#
#                     log = MailingLog(message=message, client=client, status=log_status, response=str(e) if log_status == "FAILED" else "Message sent successfully")
#                     log.save()
#
#             mailing.status = "COMPLETED"
#             mailing.save()
