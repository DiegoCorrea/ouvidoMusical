# Generated by Django 2.1 on 2018-08-04 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('NDCG', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BenchNDCG',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='NDCG.NDCG')),
                ('started_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField()),
            ],
        ),
    ]
