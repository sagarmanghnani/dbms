# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160910233805 on 2017-01-07 05:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20170106_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='datetime',
        ),
    ]
