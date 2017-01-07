
from django import forms
from .models import SignNer, EvenT
from django.forms import Textarea, PasswordInput
from datetimewidget.widgets import TimeWidget, DateWidget

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
        dateoption = {'format': 'dd/mm/yy',
                      'autoclose': True,
                      }
        timeoption = {
            'format' : 'HH:ii P',
            'autoclose' : True,
            'showMeridian' : True,
        }
        widgets = {
            'about_event' : Textarea(attrs={'cols': 80, 'rows':20}),
            'date' : DateWidget(usel10n=True, bootstrap_version=3, options=dateoption),
            'time' : TimeWidget(usel10n= True, bootstrap_version=3, options=timeoption),
            }

class ChoIce(forms.Form):
    topics = forms.ModelChoiceField(queryset=EvenT.objects.all(), widget=forms.RadioSelect)

    def __init__(self, us, *args, **kwargs):
        super(ChoIce,self).__init__(*args, **kwargs)
        self.fields['topics'].queryset = EvenT.objects.filter(user=us)

class kidhar(forms.Form):
    eventtt = forms.ModelChoiceField(queryset= EvenT.objects.all())

    def __init__(self, u, *args, **kwargs):
        super(kidhar, self).__init__(*args, **kwargs)
        self.fields['eventtt'].queryset = EvenT.objects.filter(user=u)

class DeleTe(forms.Form):
    deletion = forms.ModelMultipleChoiceField(queryset=EvenT.objects.all(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, user, *args, **kwargs):
        super(DeleTe, self).__init__(*args, **kwargs)
        self.fields['deletion'].queryset = EvenT.objects.filter(user=user)

class City(forms.Form):
    city = forms.ChoiceField(choices=[], required=None)

    def __init__(self, *args, **kwargs):
        super(City, self).__init__(*args, **kwargs)
        self.fields['city'].choices = EvenT.objects.all().values_list("eventplace", "eventplace").distinct()
