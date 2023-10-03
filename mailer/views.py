from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
from django.urls import reverse_lazy, reverse
from django.http import Http404
from django.http import HttpResponseForbidden

from mailer.forms import ClientForm, MessageForm, MailingForm, MailingLogForm
from mailer.models import Client, Mailing, Message, MailingLog

from django.db import transaction

import logging

logger = logging.getLogger(__name__)


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return Client.objects.filter(user=self.request.user)
        return Client.objects.none()  # Вместо возврата всех объектов, возвращаем пустой запрос

    # def get_queryset(self):
    #     if not self.request.user.is_anonymous:
    #         return Client.objects.filter(user=self.request.user)
    #     return Client.objects.all()


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client'

    def get_object(self, queryset=None):
        """Переопределенный метод для получения объекта, учитывая права пользователя."""
        obj = super().get_object(queryset=queryset)

        # Проверяем, принадлежит ли объект текущему пользователю
        if obj.user == self.request.user:
            return obj
        else:
            raise Http404("У вас нет прав на просмотр этого объекта.")


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailer/client_form.html'
    success_url = reverse_lazy('mailer:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailer/client_form.html'
    success_url = reverse_lazy('mailer:index')

    def get_object(self, queryset=None):
        """Переопределенный метод для получения объекта, учитывая права пользователя."""
        obj = super().get_object(queryset=queryset)

        # Проверяем, принадлежит ли объект текущему пользователю
        if obj.user == self.request.user:
            return obj
        else:
            raise Http404("У вас нет прав на редактирование этого объекта.")


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'mailer/client_confirm_delete.html'
    success_url = reverse_lazy('mailer:index')

    def get_object(self, queryset=None):
        """Переопределенный метод для получения объекта, учитывая права пользователя."""
        obj = super().get_object(queryset=queryset)

        # Проверяем, принадлежит ли объект текущему пользователю
        if obj.user == self.request.user:
            return obj
        else:
            raise Http404("У вас нет прав на удаление этого объекта.")


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailer/mailer_forms.html'
    context_object_name = 'mailing'

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return Mailing.objects.filter(user=self.request.user)
        return Message.objects.none()  # Вместо возврата всех объектов, возвращаем пустой запрос


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'client_detail.html'
    context_object_name = 'client'

    def get_object(self, queryset=None):
        """Переопределенный метод для получения объекта, учитывая права пользователя."""
        obj = super().get_object(queryset=queryset)

        # Проверяем, принадлежит ли объект текущему пользователю
        if obj.user == self.request.user:
            return obj
        else:
            raise Http404("У вас нет прав на просмотр этого объекта.")


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailer/mailing_form.html'
    success_url = reverse_lazy('mailer:create_mailing')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailer/mailing_form.html'
    success_url = reverse_lazy('mailer:create_mailing')

    def get_object(self, queryset=None):
        """Переопределенный метод для получения объекта, учитывая права пользователя."""
        obj = super().get_object(queryset=queryset)

        # Проверяем, принадлежит ли объект текущему пользователю
        if obj.user == self.request.user:
            return obj
        else:
            raise Http404("У вас нет прав на редактирование этого объекта.")


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('client_list')

    def get_object(self, queryset=None):
        """Переопределенный метод для получения объекта, учитывая права пользователя."""
        obj = super().get_object(queryset=queryset)

        # Проверяем, принадлежит ли объект текущему пользователю
        if obj.user == self.request.user:
            return obj
        else:
            raise Http404("У вас нет прав на удаление этого объекта.")


class MessageListView(ListView):
    model = Message
    template_name = 'mailer/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return Message.objects.filter(user=self.request.user)
        return Message.objects.none()  # Вместо возврата всех объектов, возвращаем пустой запрос


class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailer/message_list.html'
    context_object_name = 'messages'

    def get_object(self, queryset=None):
        """Переопределенный метод для получения объекта, учитывая права пользователя."""
        obj = super().get_object(queryset=queryset)

        # Проверяем, принадлежит ли объект текущему пользователю
        if obj.user == self.request.user:
            return obj
        else:
            raise Http404("У вас нет прав на просмотр этого объекта.")


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailer/message_form.html'
    success_url = reverse_lazy('mailer:list_message')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailer/message_form.html'
    success_url = reverse_lazy('mailer:list_message')

    def get_object(self, queryset=None):
        """Переопределенный метод для получения объекта, учитывая права пользователя."""
        obj = super().get_object(queryset=queryset)

        # Проверяем, принадлежит ли объект текущему пользователю
        if obj.user == self.request.user:
            return obj
        else:
            raise Http404("У вас нет прав на редактирование этого объекта.")


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mailer/message_confirm_delete.html'
    success_url = reverse_lazy('mailer:list_message')

    def get_object(self, queryset=None):
        """Переопределенный метод для получения объекта, учитывая права пользователя."""
        obj = super().get_object(queryset=queryset)

        # Проверяем, принадлежит ли объект текущему пользователю
        if obj.user == self.request.user:
            return obj
        else:
            raise Http404("У вас нет прав на удаление этого объекта.")

    def get_object(self, queryset=None):
        """Переопределенный метод для получения объекта, учитывая права пользователя."""
        obj = super().get_object(queryset=queryset)

        # Проверяем, принадлежит ли объект текущему пользователю
        if obj.user == self.request.user:
            return obj
        else:
            raise Http404("У вас нет прав на просмотр этого объекта.")


class MailingLogListView(ListView):
    model = MailingLog
    template_name = 'mailer/mailinglog_list.html'
    context_object_name = 'mailinglogs'

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return MailingLog.objects.filter(user=self.request.user)
        return MailingLog.objects.none()  # Вместо возврата всех объектов, возвращаем пустой запрос


class MailingLogCreateView(CreateView):
    model = MailingLog
    form_class = MailingLogForm
    template_name = 'mailer/mailinglog_form.html'
    success_url = reverse_lazy('mailer:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class CombinedCreateView(TemplateView):
    template_name = 'mailer/mailing_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_form'] = ClientForm(prefix="client")
        context['mailing_form'] = MailingForm(prefix="mailing")
        context['message_form'] = MessageForm(prefix="message")
        context['title'] = "Создать новую рассылку"
        context['text'] = "Заполните форму ниже, чтобы создать новую рассылку."  # И это
        return context

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        # Проверяем, авторизован ли пользователь
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden("У вас нет прав на создание этого объекта.")

        client_form = ClientForm(request.POST, prefix="client")
        mailing_form = MailingForm(request.POST, prefix="mailing")
        message_form = MessageForm(request.POST, prefix="message")

        if client_form.is_valid() and mailing_form.is_valid() and message_form.is_valid():

            client = client_form.save(commit=False)
            client.user = self.request.user
            client.save()
            # print(f"Client saved with ID: {client.id}")
            logger.info(f"Client saved with ID: {client.id}")

            mailing = mailing_form.save(commit=False)
            mailing.client = client
            mailing.user = self.request.user
            mailing.save()
            logger.info(f"Mailing saved with ID: {mailing.id}")

            message = message_form.save(commit=False)
            message.mailing = mailing
            message.user = self.request.user
            message.save()
            logger.info(f"Message saved with ID: {message.id}")

            return redirect('mailer:list_mailing')
        else:
            return self.render_to_response(
                self.get_context_data(client_form=client_form, mailing_form=mailing_form, message_form=message_form))


class CombinedUpdateView(TemplateView):
    template_name = 'mailer/mailing_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        client_id = self.kwargs.get('client_id')
        mailing_id = self.kwargs.get('mailing_id')
        message_id = self.kwargs.get('message_id')

        client = get_object_or_404(Client, id=client_id)
        mailing = get_object_or_404(Mailing, id=mailing_id)
        message = get_object_or_404(Message, id=message_id)

        context['client_form'] = ClientForm(prefix="client", instance=client)
        context['mailing_form'] = MailingForm(prefix="mailing", instance=mailing)
        context['message_form'] = MessageForm(prefix="message", instance=message)
        return context

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        client_id = self.kwargs.get('client_id')
        mailing_id = self.kwargs.get('mailing_id')
        message_id = self.kwargs.get('message_id')

        client_instance = get_object_or_404(Client, id=client_id)
        mailing_instance = get_object_or_404(Mailing, id=mailing_id)
        message_instance = get_object_or_404(Message, id=message_id)

        # Проверяем, принадлежат ли объекты текущему пользователю
        if not (client_instance.user == self.request.user and
                mailing_instance.user == self.request.user and
                message_instance.user == self.request.user):
            return HttpResponseForbidden("У вас нет прав на редактирование этих объектов.")

        client_form = ClientForm(request.POST, prefix="client", instance=client_instance)
        mailing_form = MailingForm(request.POST, prefix="mailing", instance=mailing_instance)
        message_form = MessageForm(request.POST, prefix="message", instance=message_instance)

        if client_form.is_valid() and mailing_form.is_valid() and message_form.is_valid():
            client_form.save()
            mailing_form.save()
            message_form.save()

            return redirect('mailer:list_mailing')
        else:
            return self.render_to_response(
                self.get_context_data(client_form=client_form, mailing_form=mailing_form, message_form=message_form))


class CombinedListView(TemplateView):
    template_name = 'mailer/mailing_list.html'

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return {
                'clients': Client.objects.filter(user=self.request.user),
                'mailings': Mailing.objects.filter(user=self.request.user),
                'messages': Message.objects.filter(user=self.request.user)
            }
        return {
            'clients': Client.objects.all(),
            'mailings': Mailing.objects.all(),
            'messages': Message.objects.all()
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context.update(queryset)
        return context


class CombinedDeleteView(View):

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        client_id = self.kwargs.get('client_id')
        mailing_id = self.kwargs.get('mailing_id')
        message_id = self.kwargs.get('message_id')

        client_instance = get_object_or_404(Client, id=client_id)
        mailing_instance = get_object_or_404(Mailing, id=mailing_id)
        message_instance = get_object_or_404(Message, id=message_id)

        # Проверяем, принадлежат ли объекты текущему пользователю
        if not (client_instance.user == self.request.user and
                mailing_instance.user == self.request.user and
                message_instance.user == self.request.user):
            return HttpResponseForbidden("У вас нет прав на удаление этих объектов.")

        # Если все проверки прошли успешно, удаляем объекты
        if client_id:
            client_instance.delete()
        if mailing_id:
            mailing_instance.delete()
        if message_id:
            message_instance.delete()

        return redirect('mailer:list_mailing')

