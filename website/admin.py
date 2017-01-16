# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from website.models import SignNer, EvenT, Question

# Register your models here.

admin.site.register(SignNer)
admin.site.register(EvenT)
admin.site.register(Question)