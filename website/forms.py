from django.contrib.auth.models import User
from django import forms
from .models import SignNer

class SignUp(forms.ModelForm):
    class Meta:
        model = SignNer
        fields = ('firstname','lastname','password','username')
