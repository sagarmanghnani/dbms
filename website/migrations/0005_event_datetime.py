# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160910233805 on 2017-01-06 09:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_signner_reg_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]