# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(db_index=True, default='c2f49392b02411e7b9ac708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
