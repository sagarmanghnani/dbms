# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import SignUp, VerIfy, EvenTform
from website.models import SignNer, EvenT
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):
    return render(request, 'website/index.html')

def registration(request):
    if request.method == 'POST':
        form = SignUp(data=request.POST)
        if form.is_valid():
            latest = form.cleaned_data
            try:
                SignNer.objects.get(username=latest['username'])
                return HttpResponse("user exist already")
            except SignNer.DoesNotExist:
                saver = form.save()
                return HttpResponse("your have been registered")
    else:
        form = SignUp()
    return render(request, 'website/register.html', {'form': form})

def verification(request):
    if request.method == 'POST':
        new_form = VerIfy(data=request.POST)
        if new_form.is_valid():
            latter = new_form.cleaned_data
            try:
                SignNer.objects.get(username=latter['username'], password=latter['password'])
                usernamer = latter['username']
                request.session['usernamer'] = usernamer
                return HttpResponseRedirect(reverse('event'))
            except SignNer.DoesNotExist:
                return HttpResponse("you may have entered wrong information")
        else:
            return HttpResponse("information is not in required format")
    else:
        new_form = VerIfy()
    return render(request, 'website/login.html', {'new_form': new_form})

def event(request):
    usernamer = request.session['usernamer']
    if request.method == 'POST':
        signer = SignNer.objects.get(username = usernamer)
        newest_form = EvenTform(data=request.POST)
        if newest_form.is_valid():
            event_form = newest_form.save(commit=False)
            event_form.user = signer
            event_form.save()
        else:
            return HttpResponse("information is not in required format")
    else:
        newest_form = EvenTform()
    return render(request, 'website/event.html', {'newest_form': newest_form, 'usernamer' : usernamer})









