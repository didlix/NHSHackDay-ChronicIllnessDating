from django.forms import ModelForm


from models import Message

class MessageForm(ModelForm):
    class Meta(object):
        model = Message
        fields = ("body",)
