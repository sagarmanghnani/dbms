from django.contrib.auth.models import User
from django import forms
from .models import SignNer

class SignUp(forms.ModelForm):
    class Meta:
        model = SignNer
        fields = ('firstname','lastname','password','username')

# creating forms for login of User

class VerIfy(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)
    
