from django.contrib.auth.models import User
from django import forms
from .models import SignNer, EvenT
from django.forms import Textarea, PasswordInput

class SignUp(forms.ModelForm):
    class Meta:
        model = SignNer
        fields = ('firstname','lastname','password','username')
        widgets = {
            'password': PasswordInput()
        }

# creating forms for login of User

class VerIfy(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)

# creating model forms for the event

class EvenTform(forms.ModelForm):
    class Meta:
        model = EvenT
        exclude = ('user',)
        widgets = {
            'about_event' : Textarea(attrs={'cols': 80, 'rows':20}),
        }
class ChoIce(forms.Form):
    topics = forms.ModelChoiceField(queryset=EvenT.objects.all(), widget=forms.RadioSelect)
    name = forms.CharField(max_length=20)

