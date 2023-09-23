from email.headerregistry import Group

from django.contrib.auth.models import AbstractUser, Permission
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    groups = models.ManyToManyField('auth.Group', blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='custom_user_set')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
