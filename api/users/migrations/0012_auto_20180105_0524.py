# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-05 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180105_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(db_index=True, default='adbc689cf1d811e7a4d2708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
