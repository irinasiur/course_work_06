from mailer.models import Client, Mailing, Message, MailingLog
from django import forms


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ('full_name', 'email')


class MailingForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ['start_time', 'periodicity']


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ('mailing', 'subject', 'body')


class MailingLogForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = MailingLog
        fields = ('message', 'client', 'status', 'response')

