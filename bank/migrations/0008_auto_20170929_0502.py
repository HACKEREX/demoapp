# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-09-29 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_auto_20170929_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankuser',
            name='bank_name',
            field=models.CharField(choices=[('1', 'SBI'), ('2', 'AXIS BANK'), ('3', 'BANK OF INDIA')], default=1, max_length=50),
        ),
    ]