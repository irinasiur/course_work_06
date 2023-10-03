from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(**NULLABLE)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)


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

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)


class Message(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)


class MailingLog(models.Model):
    STATUS_CHOICES = [
        ('SUCCESS', 'Успешно'),
        ('FAILED', 'Ошибка'),
    ]

    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    response = models.TextField(**NULLABLE)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)


