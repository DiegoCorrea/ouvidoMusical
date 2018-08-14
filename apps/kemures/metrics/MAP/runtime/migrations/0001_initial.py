# Generated by Django 2.1 on 2018-08-14 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MAP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MAPRunTime',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='MAP.MAP')),
                ('started_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField()),
            ],
        ),
    ]
