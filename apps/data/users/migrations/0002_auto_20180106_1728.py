# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-06 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(db_index=True, default='07e3f75df30711e7a4d2708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]