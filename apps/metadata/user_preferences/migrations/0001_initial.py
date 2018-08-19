# Generated by Django 2.1 on 2018-08-19 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_count', models.IntegerField(default=0)),
                ('song',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='songs.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userpreference',
            unique_together={('user', 'song')},
        ),
    ]
