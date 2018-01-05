from api.users.models import User
from api.evaluation.models import MAP, MRR, NDCG
from api.benchmark.evaluators.models import MAP as benchMAP, MRR as benchMRR, NDCG as benchNDCG
from time import gmtime, strftime
import numpy as np
import logging

logger = logging.getLogger(__name__)

def userLikeArray(recommendations):
    if len(recommendations) == 0:
        return []
    return [rec.iLike for rec in recommendations]
#####################################################################
# MAP
# Mean Averange Precision
#
#####################################################################
def getAP(relevanceArray):
    n_relevances = len(relevanceArray)
    if n_relevances == 0:
        return 0
    hitList = []
    relevant = 0
    for i in range(n_relevances):
        if relevanceArray[i]:
            relevant += 1
            hitList.append(relevant/(i+1))
    ap = sum(hitList)
    if (ap > 0):
        return sum(hitList)/relevant
    else:
        return 0
def calcUsersMAP(limit=5):
    logger.info("[Start User MAP]")
    ap = []
    for user in User.objects.all():
        userec = user.usersongrecommendation_set.all()[:limit]
        if (len(userec) == 0): continue
        ap.append(getAP(userLikeArray(userec)))
    uMap = np.mean(ap)
    logger.debug("Mean Average Precision@%d: %d", limit, uMap)
    logger.debug("Total Users Rated: %d", len(ap))
    logger.info("[Finish User MAP]")
    return uMap
def runMAP(limit=5):
    logger.info("[Start MAP Evaluation]")
    execTime = [ ]
    execTime.append(strftime("%a, %d %b %Y %X", gmtime()))
    value = calcUsersMAP(limit=limit)
    execTime.append(strftime("%a, %d %b %Y %X", gmtime()))
    bench = benchMAP(started_at=execTime[0],finished_at=execTime[1])
    bench.save()
    logger.info("Benchmark: Start at - ",execTime[0]," || Finished at -",execTime[1])
    mapResult = MAP(value=value, limit=limit)
    mapResult.save()
    logger.info("[Finish MAP Evaluation]")
#####################################################################
# MRR
#
#####################################################################
def getMRR(relevanceArray):
    n_relevances = len(relevanceArray)
    if n_relevances == 0:
        return 0
    for i in range(n_relevances):
        if relevanceArray[i]:
            return 1/(i+1)
    return 0
def calcUsersMRR(limit=5):
    logger.info("[Start User MRR]")
    mrrList = []
    for user in User.objects.all():
        userec = user.usersongrecommendation_set.all()[:limit]
        if (len(userec) == 0): continue
        mrrList.append(getAP(userLikeArray(userec)))
    uMrr = np.mean(mrrList)
    logger.debug("Mean Reciprocal Rank@%d: %d", limit, uMrr)
    logger.debug("Total Users Rated: %d", len(mrrList))
    logger.info("[Finish User MRR]")
    return uMrr
def runMRR(limit=5):
    execTime = [ ]
    logger.info("[Start MRR Evaluation]")
    execTime.append(strftime("%a, %d %b %Y %X", gmtime()))
    value = calcUsersMRR(limit=limit)
    execTime.append(strftime("%a, %d %b %Y %X", gmtime()))
    bench = benchMAP(started_at=execTime[0],finished_at=execTime[1])
    bench.save()
    logger.info("Benchmark: Start at - ",execTime[0]," || Finished at -",execTime[1])
    mrrResult = MRR(value=value, limit=limit)
    mrrResult.save()
    logger.info("[Finish MRR Evaluation]")
#####################################################################
# NDCG
#
#####################################################################
""" Reference from https://gist.github.com/bwhite/3726239
"""
def dcg_at_k(r, k, method=0):
    r = np.asfarray(r)[:k]
    if r.size:
        if method == 0:
            return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
        elif method == 1:
            return np.sum(r / np.log2(np.arange(2, r.size + 2)))
        else:
            raise ValueError('method must be 0 or 1.')
    return 0.


def ndcg_at_k(r, k, method=0):
    dcg_max = dcg_at_k(sorted(r, reverse=True), k, method)
    if not dcg_max:
        return 0.
    return dcg_at_k(r, k, method) / dcg_max

def calcUsersNDCG(limit=5):
    logger.info("[Start Users NDCG]")
    result = [ndcg_at_k(userScoreList(user.usersongrecommendation_set.all()),k=limit, method=0) for user in User.objects.all()]
    uNDCG = np.mean(result)
    logger.debug("Normalized Cumulative Gain@%d: %d", limit, uNDCG)
    logger.debug("Total Users Rated: %d", len(result))
    logger.info("[Finish Users NDCG]")
    return uNDCG

def userScoreList(recommendations):
    if len(recommendations) == 0:
        return []
    return [rec.score for rec in recommendations]

def runNDCG(limit=5):
    execTime = [ ]
    logger.info("[Start NDCG Evaluation]")
    execTime.append(strftime("%a, %d %b %Y %X",gmtime()))
    value = calcUsersNDCG(limit=limit)
    execTime.append(strftime("%a, %d %b %Y %X",gmtime()))
    bench = benchNDCG(started_at=execTime[0],finished_at=execTime[1])
    bench.save()
    logger.info("Benchmark: Start at - ",execTime[0]," || Finished at -",execTime[1])
    ndcgResult = NDCG(value=value,limit=limit)
    ndcgResult.save()
    logger.info("[Finish NDCG Evaluation]")
################################################################################
def runEvaluateUsersRank(limit=5):
    runMAP(limit=limit)
    runMRR(limit=limit)
    runNDCG(limit=limit)
