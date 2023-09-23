from django.db import models

from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)


class Mailing(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'Создана'),
        ('RUNNING', 'Запущена'),
        ('COMPLETED', 'Завершена'),
    ]

    PERIODICITY_CHOICES = [
        ('DAILY', 'Раз в день'),
        ('WEEKLY', 'Раз в неделю'),
        ('MONTHLY', 'Раз в месяц'),
    ]

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    periodicity = models.CharField(max_length=10, choices=PERIODICITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CREATED')


class Message(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()


class MailingLog(models.Model):
    STATUS_CHOICES = [
        ('SUCCESS', 'Успешно'),
        ('FAILED', 'Ошибка'),
    ]

    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    response = models.TextField(blank=True, null=True)

