from django.urls import path

from mailer.apps import MailerConfig
from mailer.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, MessageListView, \
    MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView

app_name = MailerConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='index'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/add/', ClientCreateView.as_view(), name='client_add'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/add/', MailingCreateView.as_view(), name='mailing_add'),
    path('mailing/<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_edit'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/add/', MessageCreateView.as_view(), name='message_add'),
    path('message/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_edit'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

]