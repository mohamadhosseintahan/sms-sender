from django import forms
from Base.models import Message

class SMSForm (forms.ModelForm):
    class Meta:
        model = Message
        fields = ('receptor' , 'message',)