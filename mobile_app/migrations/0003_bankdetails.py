# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-09-29 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0002_auto_20170929_0435'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_ph_no', models.CharField(max_length=13)),
                ('registered_account', models.CharField(max_length=11)),
                ('registered_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile_app.AppUser')),
            ],
        ),
    ]
