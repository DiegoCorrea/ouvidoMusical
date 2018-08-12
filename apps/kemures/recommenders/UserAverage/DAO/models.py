# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.metadata.users.models import User
from apps.metadata.songs.models import Song


class UserAverageLife(models.Model):
    song_model_size = models.IntegerField()


class UserAverageRecommendations(models.Model):
    # IDS
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, unique=False, on_delete=models.CASCADE)
    life = models.ForeignKey(UserAverageLife, unique=False, on_delete=models.CASCADE)
    # Datas
    similarity = models.FloatField(default=0.0, unique=False)
    iLike = models.BooleanField(default=False)
    score = models.IntegerField(blank=True, null=True, unique=False)
    # Timers
    created_at = models.DateTimeField(auto_now_add=True)

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
