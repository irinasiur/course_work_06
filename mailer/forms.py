from mailer.models import Client, Mailing, Message, MailingLog
from django import forms
from django.forms import ModelForm, DateTimeInput
from django.utils import timezone

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
        fields = ['start_time', 'end_time', 'periodicity']
        widgets = {
            'start_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_start_time(self):
        start_time = self.cleaned_data.get('start_time')
        # Если start_time не None и является "наивным" объектом datetime,
        # делаем его "осведомленным" относительно текущего часового пояса.
        if start_time and timezone.is_naive(start_time):
            start_time = timezone.make_aware(start_time)
        return start_time

    def clean_end_time(self):
        end_time = self.cleaned_data.get('end_time')
        # Аналогично для end_time.
        if end_time and timezone.is_naive(end_time):
            end_time = timezone.make_aware(end_time)
        return end_time


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'body')


class MailingLogForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = MailingLog
        fields = ('message', 'client', 'status', 'response')

