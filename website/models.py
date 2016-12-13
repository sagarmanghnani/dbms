# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db import models

# Create your models here.

class SignNer(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username

