# Generated by Django 2.1 on 2018-08-04 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180804_2025'),
        ('songs', '0002_auto_20180804_2025'),
        ('user_preferences', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPreferences',
            new_name='UserPreference',
        ),
    ]
