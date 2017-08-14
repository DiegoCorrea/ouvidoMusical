# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.
class Song(models.Model):
    song = models.CharField(max_length=255, unique=True, db_index=True, primary_key=True, default=uuid.uuid1().hex)

    title = models.CharField(max_length=255, unique=False)
    album = models.CharField(max_length=255, unique=False)
    artist = models.CharField(max_length=255, unique=False)
    year = models.IntegerField(default=0, unique=False)

    def as_json(self):
        return dict(
            song_id = self.song,
            title = self.title,
            album = self.album,
            artist = self.artist,
            year = self.year)

class User(models.Model):
    user = models.CharField(max_length=255, unique=True, db_index=True, primary_key=True, default=uuid.uuid1().hex)

    def as_json(self):
        return dict(
            user_id = self.user)

class UserPlaySong(models.Model):
    user = models.ForeignKey(User, unique=False)
    song = models.ForeignKey(Song, unique=False)
    play_count = models.IntegerField(default=0, unique=False)

    def as_json(self):
        return dict(
            song_id = self.song_id,
            user_id = self.user_id,
            play_count = self.play_count)

class UserSongRecommendation(models.Model):
    user = models.ForeignKey(User, unique=False)
    song = models.ForeignKey(Song, unique=False)
    probabilit_play_count = models.IntegerField(default=0, unique=False)

    def as_json(self):
        return dict(
            song_id = self.song_id,
            user_id = self.user_id,
            probabilit_play_count = self.probabilit_play_count)
