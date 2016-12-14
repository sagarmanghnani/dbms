from django.contrib.auth.models import User
from django import forms
from .models import SignNer, EvenT

class SignUp(forms.ModelForm):
    class Meta:
        model = SignNer
        fields = ('firstname','lastname','password','username')

# creating forms for login of User

class VerIfy(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)

# creating model forms for the event

class EvenTform(forms.ModelForm):
    class Meta:
        model = EvenT
        exclude = ('user',)
    
