# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from website.forms import SignUp
from website.models import SignNer

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

