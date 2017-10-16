# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from api.users.models import User
from api.songs.models import Song

# Create your models here.
class UserSongRecommendation(models.Model):
    user = models.ForeignKey(User, unique=False)
    song = models.ForeignKey(Song, unique=False)
    similarity = models.IntegerField(default=0, unique=False)
    iLike = models.BooleanField(default=False)
    score = models.IntegerField(blank=True, null=True, unique=False)

    class Meta:
        unique_together = (('user', 'song'),)

    def as_json(self):
        return dict(
            song_id=self.song_id,
            user_id=self.user_id,
            similarity=self.similarity,
            iLike=self.iLike,
            score=self.score
        )