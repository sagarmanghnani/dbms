# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160910233805 on 2017-01-22 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_event_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signner',
            name='userimg',
            field=models.FileField(blank=True, null=True, upload_to='user/'),
        ),
    ]
