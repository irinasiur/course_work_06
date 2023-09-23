from django.contrib import admin

from mailer.models import Client, Mailing, Message, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'comment']
    search_fields = ['email', 'full_name']
    list_filter = ['email']
    ordering = ['full_name']


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'periodicity', 'status']
    list_filter = ['periodicity', 'status']
    ordering = ['start_time']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'body']
    search_fields = ['subject']
    ordering = ['subject']


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ['client', 'message', 'attempt_time', 'status', 'response']
    list_filter = ['status']
    ordering = ['-attempt_time']
