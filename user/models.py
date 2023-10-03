from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class CustomUserManager(BaseUserManager):
    """
    Custom manager for User.
    """
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    groups = models.ManyToManyField('auth.Group', blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='custom_user_set')

    objects = CustomUserManager()  # Используйте ваш собственный менеджер

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




