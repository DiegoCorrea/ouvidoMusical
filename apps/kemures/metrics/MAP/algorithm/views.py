from .algorithm import calcUsersMAP
from .models import MAP
from apps.kemures.metrics import BenchMAP
from django.utils import timezone
from apps.kemures.recommenders.UserAverage import UserAverage_Life

import logging
logger = logging.getLogger(__name__)


def runMAP(at):
    logger.info("[Start MAP Evaluation]")
    startedAt = timezone.now()
    value = calcUsersMAP(at=at)
    finishedAt = timezone.now()
    mapResult = MAP(
        life=UserAverage_Life.objects.last(),
        value=value,
        at=at
    )
    mapResult.save()
    BenchMAP.objects.create(
        id=mapResult,
        started_at=startedAt,
        finished_at=finishedAt
    )
    logger.info(
        "Benchmark: Start at - "
        + str(startedAt)
        + " || Finished at -"
        + str(finishedAt)
    )
    logger.info("[Finish MAP Evaluation]")