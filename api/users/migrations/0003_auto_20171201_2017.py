# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171201_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(db_index=True, default='9bcfc31ed6d411e7baff708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]