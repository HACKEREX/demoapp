# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-09-29 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='google_play_account',
            field=models.URLField(max_length=128),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='user_name',
            field=models.CharField(max_length=150),
        ),
    ]
