# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-02 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0008_transaction_transaction_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_withdrawl',
            field=models.CharField(choices=[('1', 'PENDING'), ('2', 'COMPLETED')], default='1', max_length=20),
        ),
    ]
