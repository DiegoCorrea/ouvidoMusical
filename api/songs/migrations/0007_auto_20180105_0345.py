# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-05 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_auto_20180105_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.CharField(db_index=True, default='e0840181f1ca11e7a4d2708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
