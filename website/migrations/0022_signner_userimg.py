# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160910233805 on 2017-01-20 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_event_event_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='signner',
            name='userimg',
            field=models.FileField(null=True, upload_to='user/'),
        ),
    ]
