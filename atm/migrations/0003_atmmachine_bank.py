# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-09-30 06:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0011_remove_bank_atms'),
        ('atm', '0002_auto_20170930_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='atmmachine',
            name='bank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bank.Bank'),
        ),
    ]
