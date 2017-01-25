# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160910233805 on 2017-01-24 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_auto_20170122_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
            options={
                'indexes': [],
            },
        ),
    ]
