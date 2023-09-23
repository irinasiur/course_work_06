import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from user.forms import UserRegisterForm, UserForm
from user.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем, до окончания регистрации осталось совсем чуть-чуть',
            message='Для завершения регистрации перейдите по ссылке http://127.0.0.1:8000/',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('mailer:index')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('mailer:index'))
