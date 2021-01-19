from django import forms
from Base.models import Message

class SMSForm (forms.ModelForm):
    class Meta:
        model = Message
        fields = ('receptor' , 'message',)
        

    def clean_receptor(self) :
        receptor = self.cleaned_data['receptor']

        if len(str(receptor)) != 10 : 
            print(len(str(receptor)))
            print(str(receptor))
            raise forms.ValidationError('phone number is invalid!')
        return receptor