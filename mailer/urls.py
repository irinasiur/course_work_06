from django.urls import path

from mailer.apps import MailerConfig
from mailer.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, MessageListView, \
    MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingLogCreateView, CombinedListView, \
    CombinedUpdateView, CombinedCreateView, CombinedDeleteView, MailingLogListView
from user.views import generate_new_password

app_name = MailerConfig.name

urlpatterns = [
    path('client', ClientListView.as_view(), name='list_client'),
    path('client/<int:pk>/detail/', ClientDetailView.as_view(), name='detail_client'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='update_client'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='delete_client'),

    path('message/', MessageListView.as_view(), name='list_message'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='detail_message'),
    path('message/create/', MessageCreateView.as_view(), name='create_message'),
    path('message/<int:pk>/edit/', MessageUpdateView.as_view(), name='update_message'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='delete_message'),

    path('mailinglog/', MailingLogListView.as_view(), name='list_mailinglog'),
    path('mailinglog/create/', MailingLogCreateView.as_view(), name='create_mailinglog'),

    path('combined/', CombinedListView.as_view(), name='list_mailing'),
    path('combined/create/', CombinedCreateView.as_view(), name='create_combined'),
    path('combined/delete/<int:client_id>/<int:mailing_id>/<int:message_id>/', CombinedDeleteView.as_view(), name='delete_combined'),
    path('combined/update/<int:client_id>/<int:mailing_id>/<int:message_id>/', CombinedUpdateView.as_view(), name='update_combined'),

    path('profile/genpassword', generate_new_password, name='generate_new_password'),
]