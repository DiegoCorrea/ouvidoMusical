from .songSimilarity import runTitleSimilarity
from .recommenders import runUserAverage
from .evaluation import runEvaluateUsersRank
import logging
logger = logging.getLogger(__name__)

def bigBang():
    logger.info("[Start Big Bang]")
    # Calc Similarity
    runTitleSimilarity()
    # Calc Recommendations
    runUserAverage()
    # Calc Evaluations
    runEvaluateUsersRank()
    logger.info("[Finish Big Bang]")
