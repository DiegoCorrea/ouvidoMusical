# Generated by Django 2.1 on 2018-09-09 23:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CosineSimilarityRunTime', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cosinesimilarityruntime',
            name='song_set_size',
        ),
    ]
