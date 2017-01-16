
from django import forms
from .models import SignNer, EvenT, Question
from django.forms import Textarea, PasswordInput
from datetimewidget.widgets import TimeWidget, DateWidget
from django.core.exceptions import ValidationError

class SignUp(forms.ModelForm):
    renterpassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = SignNer
        fields = ('firstname','lastname','password','username', 'email')
        widgets = {
            'password': PasswordInput(render_value=False)
        }
    MIN_LENGTH = 8
    def clean(self):
        password = self.cleaned_data['password']
        know = self.cleaned_data['renterpassword']

        if len(password) < self.MIN_LENGTH and password != know:
            raise forms.ValidationError("enter %d password and confirm password does not match" %self.MIN_LENGTH)
        elif password != know:
            raise forms.ValidationError("enter password does not match")
        elif len(password) < self.MIN_LENGTH:
            raise forms.ValidationError("enter %d password" %self.MIN_LENGTH)
        return self.cleaned_data



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

class Create_quest(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', )

class Quest_choice(forms.Form):
    quest_choice = forms.ModelChoiceField(queryset=Question.objects.all())
    answer = forms.CharField(max_length=200)

class get_user(forms.Form):
    email = forms.EmailField(max_length=200)
    username = forms.CharField(max_length=200)

class Verify_user(forms.Form):
    question = forms.ChoiceField(choices=[])
    answer = forms.CharField(max_length=200)

    def __init__(self,user,*args, **kwargs):
        super(Verify_user,self).__init__(*args, **kwargs)
        self.fields['question'].choices = SignNer.objects.filter(username=user).values_list("reg_question", "reg_question").distinct()

class Assignpass(forms.Form):
    password = forms.CharField(max_length=200)
    confirm_password = forms.CharField(max_length=200)
    class Meta:
        widgets = {
            'password': PasswordInput(render_value=False)
        }

    MIN_LENGTH = 8

    def clean(self):
        password = self.cleaned_data['password']
        know = self.cleaned_data['confirm_password']

        if len(password) < self.MIN_LENGTH and password != know:
            raise forms.ValidationError("enter %d password and confirm password does not match" % self.MIN_LENGTH)
        elif password != know:
            raise forms.ValidationError("enter password does not match")
        elif len(password) < self.MIN_LENGTH:
            raise forms.ValidationError("enter %d password" % self.MIN_LENGTH)
        return self.cleaned_data
