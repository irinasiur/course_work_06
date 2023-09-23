from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from mailer.forms import ClientForm
from mailer.models import Client, Mailing, Message


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
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('client_list')


class MailingListView(ListView):
    model = Mailing
    template_name = 'client_list.html'
    context_object_name = 'clients'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'client_detail.html'
    context_object_name = 'client'


class MailingCreateView(CreateView):
    model = Mailing
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('client_list')


class MessageListView(ListView):
    model = Message
    template_name = 'client_list.html'
    context_object_name = 'clients'


class MessageDetailView(DetailView):
    model = Message
    template_name = 'client_detail.html'
    context_object_name = 'client'


class MessageCreateView(CreateView):
    model = Message
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('client_list')