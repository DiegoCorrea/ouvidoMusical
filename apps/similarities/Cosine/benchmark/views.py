import matplotlib.pyplot as plt
import logging
import os

from random import sample
from django.utils import timezone
from apps.CONSTANTS import TOTAL_RUN, SET_SIZE
from apps.data.songs.models import Song
from apps.similarities.Cosine.algorithm.algorithm import CosineSimilarity
from apps.similarities.Cosine.benchmark.models import BenchCosine_SongTitle

logger = logging.getLogger(__name__)


def CosineBenchmark(allSongs):
    logger.info("[Start Bench Cosine]")
    startedAt = timezone.now()
    similarityMatrix = CosineSimilarity([song.title for song in allSongs])
    finishedAt = timezone.now()
    similaritySum = 0.0
    countTotal = 0.0
    for line in range(len(allSongs)):
        for column in range(line, len(allSongs)):
            countTotal += 1.0
            similaritySum += similarityMatrix[line][column]
    BenchCosine_SongTitle.objects.create(
        setSize=len(allSongs),
        similarity=(similaritySum/countTotal),
        started_at=startedAt,
        finished_at=finishedAt
    )
    logger.info("[Finish Bench Cosine]")


def RunCosineBenchmark(size_list=SET_SIZE):
    logger.info("[Start Run Bench Cosine]")
    songs_list = Song.objects.all()
    for runner in size_list:
        for i in range(TOTAL_RUN):
            logger.info(
                "#########################################################"
                + "\n\t Tamanho do banco ("
                + str(runner)
                + ") Ciclo: "
                + str(i)
                + "#########################################################"
            )
            CosineBenchmark(allSongs=sample(set(songs_list), runner))
    logger.info("[Finish Run Bench Cosine]")
