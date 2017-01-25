# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import SignUp, VerIfy, EvenTform, ChoIce,kidhar,DeleTe,City,Create_quest,Quest_choice,get_user,Verify_user, Assignpass
from django.core.urlresolvers import reverse
import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from website.models import SignNer, EvenT, Question



# Create your views here.

loggedin = False

def index(request):
    if loggedin is False:
        return render(request, 'website/index.html')
    else:
        return HttpResponse("user logged in already")

def registration(request):
    if loggedin is False:
        if request.method == 'POST':
            form = SignUp(request.POST, request.FILES)
            if form.is_valid():
                latest = form.cleaned_data

                try:
                    SignNer.objects.get(username=latest['username'])
                    return HttpResponse("user exist already")
                except SignNer.DoesNotExist:
                    up_form = form.save(commit=False)
                    up_form.password = make_password(form.cleaned_data['password'])
                    up_form.save()
                    return HttpResponse("you have been registered")
        else:
            form = SignUp()
        return render(request, 'website/register.html', {'form': form})
    else:
        return HttpResponse("user is logged in")

def verification(request):
    if loggedin is False:
        if request.method == 'POST':
            new_form = VerIfy(data=request.POST)
            if new_form.is_valid():
               latter = new_form.cleaned_data
               try:
                   s1 = SignNer.objects.get(username=latter['username'])
                   checking = check_password(latter['password'], s1.password)
                   if checking:
                       usernamer = latter['username']
                       request.session['usernamer'] = usernamer
                       global loggedin
                       loggedin = True
                       return HttpResponseRedirect(reverse('website:showevents'))
                   else:
                       return HttpResponse("you might have entered wrong username or password")
               except SignNer.DoesNotExist:
                   return HttpResponse("entered wrong information")
        else:
            new_form = VerIfy()
        return render(request, 'website/login.html', {'new_form': new_form})
    else:
        return HttpResponse("user is tottaly logged in")

def event(request):
    if loggedin is True:
        usernamer = request.session['usernamer']
        if request.method == 'POST':
            signer = SignNer.objects.get(username = usernamer)
            newest_form = EvenTform(request.POST, request.FILES)

            if newest_form.is_valid():

                event_form = newest_form.save(commit=False)
                event_form.user = signer
                event_form.save()
            else:
                return HttpResponse("information is not in required format")
        else:
            newest_form = EvenTform()
        return render(request, 'website/event.html', {'newest_form': newest_form, 'usernamer' : usernamer})
    else:
        return HttpResponse("user is not logged in")

def showevents(request):
    if loggedin is True:
        usernamer = request.session['usernamer']
        sh_event = EvenT.objects.filter(Q(user=SignNer.objects.get(username=usernamer)) & Q(flag=True))
        return render(request, 'website/showevent.html', {'sh_event': sh_event})
    else:
        return HttpResponse("no user to show event")

def demo(request):
    usernamer = request.session['usernamer']
    if loggedin is True:
        global loggedin
        loggedin = False
        del request.session['usernamer']
        del usernamer
        return HttpResponseRedirect(reverse('website:index'))
    else:
        return HttpResponse("error occured")

# need by edit_form below to select the city
def trial(request):
    if loggedin is True:
        usernamer = request.session['usernamer']
        if request.method == 'POST':
            kail = ChoIce(data=request.POST, us=SignNer.objects.get(username=usernamer))
            if kail.is_valid():
                lagad = kail.cleaned_data
                kabad = lagad['topics']
                lappad = kabad.eventname
                request.session['lappad'] = lappad
                return HttpResponse("received" + kabad.eventplace)
            else:
                return HttpResponse("data is not in required format")
        else:
            kail = ChoIce(us=SignNer.objects.get(username=usernamer))
        return render(request, 'website/trial.html', { 'kail' : kail,'usernamer' : usernamer })
    else:
        return HttpResponse("user is not logged in")


"""def edit_form(request):
    if loggedin is True:
        lappad = request.session['lappad']
        thappad = EvenT.objects.get(eventname= lappad)
        if request.method == 'POST':
            keyform = EvenTform(data=request.POST, instance=thappad)
            if keyform.is_valid():
                saver = keyform.save()
                return HttpResponse("information edited")
            else:
                return HttpResponse("information not in desired format")
        else:
            keyform = EvenTform(instance=thappad)
        return render(request, 'website/edit.html', {'thappad' : thappad, 'lappad' : lappad, 'keyform' : keyform})
    else:
        return HttpResponse("user is not logged in")"""

def another(request):
    usernamer = request.session['usernamer']
    if request.method == 'POST':
        d = kidhar(u=SignNer.objects.get(username=usernamer))
    else:
        d = kidhar(u=SignNer.objects.get(username=usernamer))
        return render(request, 'website/another.html', {'usernamer' : usernamer, 'd' : d})


def delete(request):
    if loggedin is True:
        usernamer = request.session['usernamer']
        if request.method == 'POST':
            form = DeleTe(data=request.POST, user=SignNer.objects.get(username=usernamer))
            if form.is_valid():
                new_form = form.cleaned_data
                get_object = new_form['deletion']
                for obj in get_object:
                    obj.delete()
                return HttpResponse("your events are deleted")
            else:
                return HttpResponse("information invalid")
        else:
            form = DeleTe(user=SignNer.objects.get(username=usernamer))
            return render(request, 'website/delete.html', {'usernamer' : usernamer, 'form' : form})
    else:
        return HttpResponse("user is not logged in")

# started again from here putting flag value to true

def city_val(request):
    if loggedin is True:
        if request.method == "POST":
            form =  City(data=request.POST)

            if form.is_valid():
                new_form = form.cleaned_data
                namer = new_form['city']
                request.session['namer'] = namer
                return HttpResponse("here it is " + namer )
            else:
                return HttpResponse("information is not in order")
        else:
            form = City()
            return render(request, 'website/city.html', {'form' : form})
    else:
        return HttpResponse("user not logged in")

def city_events(request):
    if loggedin is True:
        namer = request.session['namer']
        events_city = EvenT.objects.filter(eventplace=namer)
        return render(request, 'website/cityevents.html', {'namer' : namer, 'events_city' : events_city})
    else:
        return HttpResponse("user not logged in")

def details_event(request, city_id):
    if loggedin is True:
        sub = EvenT.objects.get(id = city_id)
        return render(request, 'website/citydetail.html', {'sub' : sub})
    else:
        return HttpResponse("user not logged in")

def show_reg_events(request):
    if loggedin is True:
        usernamer = request.session['usernamer']
        s2 = SignNer.objects.get(username=usernamer)
        e1 = EvenT.objects.filter(~Q(user = s2) & ~Q(flag=False))
        e3 = EvenT.objects.filter(id__in = s2.reg_event.all())
        reg_eventing = e1.exclude(id__in = e3)
        if reg_eventing:
            return render(request, 'website/regevents.html', {'reg_eventing' : reg_eventing, 's2' : s2, 'e1' : e1, 'e3' : e3 })
        else:
            return HttpResponse("No event to register for")
    else:
        return HttpResponse("user not logged in")
def registerevent(request, event_id):
    if loggedin is True:
        if request.method == 'POST':
            usernamer = request.session['usernamer']
            signner_obj = SignNer.objects.get(username=usernamer)
            event_obj = EvenT.objects.get(id= event_id)
            signner_obj.reg_event.add(event_obj)
            return HttpResponse("you are registered for the event")
        else:
            sub = EvenT.objects.get(id = event_id)
            return render(request, 'website/citydetail.html', {'sub' : sub})
    else:
        return HttpResponse("user not logged in")

def user_event(request):
    if loggedin is True:
        usernamer = request.session['usernamer']
        s1 = SignNer.objects.get(username=usernamer)
        e1 = s1.reg_event.all()
        if e1:
            return render(request, 'website/userevent.html', {'e1':e1, 's1':s1, 'usernamer': usernamer})
        else:
            return HttpResponse("you have not registered for any event")
    else:
        return HttpResponse("user not logged in")

def leavemeetup(request, leave_id):
    if loggedin is True:
        usernamer = request.session['usernamer']
        s2 = SignNer.objects.get(username=usernamer)
        e2 = s2.reg_event.get(id=leave_id)
        if request.method == 'POST':
            s2.reg_event.remove(e2)
            return HttpResponse("you have successfully leave the meetup")
        else:
            return render(request, 'website/leavemeet.html', {'usernamer' : usernamer,'s2' : s2, 'e2' : e2})
    else:
        return HttpResponse("user not logged in")

def upcomingevent(request):
    if loggedin is True:
        try:
            today = datetime.date.today()
            e1 = EvenT.objects.filter(date__month=today.month)
            return render(request, 'website/upcoming.html', {'today' : today, 'e1' : e1})
        except EvenT.DoesNotExist:
            return HttpResponse("There is no event in this month")
    else:
        return HttpResponse("user not logged in")

def get_quest(request):

    if request.method == 'POST':
        form = Create_quest(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("question registered")
        else:
            return HttpResponse("question cant be registered")
    else:
        form = Create_quest()
        return render(request, 'website/question.html', {'form' : form})

def sel_choice(request):

    usernamer = request.session['usernamer']
    if request.method == 'POST':
        form = Quest_choice(data=request.POST)
        if form.is_valid():
            new_quest = form.cleaned_data
            question = new_quest['quest_choice']
            answering = new_quest['answer']
            new_question = question.question
            sign = SignNer.objects.get(username=usernamer)
            sign.reg_question = new_question
            sign.answer = answering
            sign.save()
            return HttpResponse(new_question)
        else:
            return HttpResponse("wrong info")
    else:
        form = Quest_choice()
        return render(request, 'website/selchoice.html', {'form':form})

def getting_user(request):

    if request.method == 'POST':
        form = get_user(data=request.POST)
        if form.is_valid():
            latest = form.cleaned_data
            try:
                sign = SignNer.objects.get(Q(email=latest['email']) | Q(username=latest['username']))
                savesign = sign.username
                request.session['savesign'] = savesign


                return HttpResponse("your details might be found")
            except SignNer.DoesNotExist:
                return HttpResponse("information is not correct")
        else:
            return HttpResponse("information not in order")
    else:
        form = get_user()
        return render(request, 'website/getuser.html', {'form':form})

def verifyuser(request):

    savesign = request.session['savesign']
    if request.method == 'POST':
        form = Verify_user(data=request.POST,user=savesign)
        if form.is_valid():
            latest = form.cleaned_data
            sign = SignNer.objects.get(username=savesign)
            if latest['answer'] == sign.answer:
                # redirect user to newpassword
                newuser = savesign
                request.session['newuser'] = newuser
                return HttpResponse("you are verified")
            else:
                return HttpResponse("wrong answer try again")
        else:
            return HttpResponse("invalid")
    else:
        form = Verify_user(user=savesign)
        return render(request, 'website/verifyuser.html', {'form' : form, 'savesign' : savesign})

def newpassword(request):

    newuser = request.session['newuser']
    if request.method == 'POST':
        form = Assignpass(data=request.POST)
        if form.is_valid():
            sign = SignNer.objects.get(username=newuser)
            hashpass = make_password(form.cleaned_data['password'])
            sign.password = hashpass
            sign.save()
            return HttpResponse("password changed")

    else:
        form = Assignpass()
    return render(request, 'website/newpassword.html', {'form':form, 'newuser':newuser})

def redirecting(request):

    return render_to_response('website/event-main.html')

def showdel(request, del_id):
    if loggedin is True:
        events = EvenT.objects.get(id=del_id)
        events.flag = False
        events.save()
        return HttpResponseRedirect(reverse('website:showevents'))
    else:
        return HttpResponse("user not logged in")


def edit_form(request, edit_id):
    if loggedin is True:
        usernamer = request.session['usernamer']
        events = EvenT.objects.get(Q(user=SignNer.objects.get(username=usernamer)) & Q(id=edit_id))
        if request.method == 'POST':
            form = EvenTform(data=request.POST, instance=events)
            if form.is_valid():
                 form.save()
                 return HttpResponse("information edited")
            else:
                return HttpResponse("information not in desired format")
        else:
            form = EvenTform(instance=events)
            return render(request, 'website/newedit.html', {'form':form})
    else:
        return HttpResponse("user not logged in")

def all_event(request):
    if loggedin is True:
        usernamer = request.session['usernamer']
        events = EvenT.objects.filter(Q(flag=True) & ~Q(user=SignNer.objects.get(username=usernamer)))
        return render(request, 'website/allevent.html', {'events':events})
    else:
        return HttpResponse("user not logged in")
def userprofile(request):
    if loggedin is True:
        usernamer = request.session['usernamer']
        sign = SignNer.objects.get(username=usernamer)
        return render(request, 'website/userprofile.html', {'sign':sign})
    else:
        return HttpResponse("user not logged in")


def eventings(request):
    usernamer = request.session['usernamer']
    events = EvenT.objects.exclude(Q(flag=False,user=(SignNer.objects.get(username=usernamer))))
    return render(request, 'website/trying.html', {'events':events})
