# Generated by Django 2.1 on 2018-08-12 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('songs', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAverageLife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_model_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAverageRecommendations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity', models.FloatField(default=0.0)),
                ('iLike', models.BooleanField(default=False)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('life', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAverange.UserAverageLife')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='useraveragerecommendations',
            unique_together={('user', 'song')},
        ),
    ]