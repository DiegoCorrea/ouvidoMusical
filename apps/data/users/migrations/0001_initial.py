# Generated by Django 2.1 on 2018-08-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(db_index=True, default='a9a9ed2597f511e89383c569513f40c7', max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
