from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from mailer.forms import ClientForm, MessageForm, MailingForm, MailingLogForm
from mailer.models import Client, Mailing, Message, MailingLog


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailer/client_form.html'
    success_url = reverse_lazy('mailer:index')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailer/client_form.html'
    success_url = reverse_lazy('mailer:index')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'mailer/client_confirm_delete.html'
    success_url = reverse_lazy('mailer:index')


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailer/mailer_forms.html'
    context_object_name = 'mailing'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'client_detail.html'
    context_object_name = 'client'


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailer/mailing_form.html'
    success_url = reverse_lazy('mailer:create_mailing')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('mailer:mailing_edit')


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('client_list')


class MessageListView(ListView):
    model = Message
    template_name = 'mailer/message_list.html'
    context_object_name = 'messages'


class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailer/message_list.html'
    context_object_name = 'messages'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailer/message_form.html'
    success_url = reverse_lazy('mailer:list_message')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailer/message_form.html'
    success_url = reverse_lazy('mailer:list_message')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mailer/message_confirm_delete.html'
    success_url = reverse_lazy('mailer:list_message')


class MailingLogCreateView(CreateView):
    model = MailingLog
    form_class = MailingLogForm
    template_name = 'mailer/mailinglog_form.html'
    success_url = reverse_lazy('mailer:create_mailing')


class CombinedListView(ListView):
    template_name = 'combined_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['messages'] = Message.objects.all()
        context['mailings'] = Mailing.objects.all()
        return context
