# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160910233805 on 2017-01-15 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_delete_answering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=200)),
                ('question2', models.CharField(max_length=200)),
                ('answer1', models.CharField(max_length=200)),
                ('answer2', models.CharField(max_length=200)),
            ],
            options={
                'indexes': [],
            },
        ),
    ]