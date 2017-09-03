# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0007_auto_20170902_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.CharField(db_index=True, default=b'b34c0cfe905311e783064c0f6e2da75d', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.CharField(db_index=True, default=b'b34c0cff905311e783064c0f6e2da75d', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='usersongrecommendation',
            name='iLike',
            field=models.BooleanField(default=False),
        ),
    ]