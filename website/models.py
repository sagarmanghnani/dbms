# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# article
class SignNer(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    reg_event = models.ManyToManyField("EvenT")

    def __str__(self):
        return self.username


# publications
class EvenT(models.Model):
    user = models.ForeignKey(SignNer, on_delete=models.CASCADE)
    eventname = models.CharField(max_length=40)
    eventplace = models.CharField(max_length = 50)
    about_event = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)


    def __str__(self):
        return self.eventname





