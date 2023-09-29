from django.urls import path

from mailer.apps import MailerConfig
from mailer.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, MessageListView, \
    MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingLogCreateView, CombinedListView

app_name = MailerConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='index'),
    path('client/<int:pk>/detail/', ClientDetailView.as_view(), name='detail_client'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='update_client'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='delete_client'),

    path('mailing/', MailingListView.as_view(), name='mailer_forms'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/create/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing/<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_edit'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),

    path('message/', MessageListView.as_view(), name='list_message'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='detail_message'),
    path('message/create/', MessageCreateView.as_view(), name='create_message'),
    path('message/<int:pk>/edit/', MessageUpdateView.as_view(), name='update_message'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='delete_message'),

    path('mailinglog/create/', MailingLogCreateView.as_view(), name='create_mailinglog'),
    path('combined/', CombinedListView.as_view(), name='list_combined'),

]