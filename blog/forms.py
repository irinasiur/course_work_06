from blog.models import Post
from mailer.forms import StyleFormMixin
from django import forms


class PostForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
