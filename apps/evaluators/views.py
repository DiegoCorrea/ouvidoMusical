from .MAP.algorithm.views import runMAP
from .MRR.algorithm.views import runMRR
from .NDCG.algorithm.views import runNDCG
from .MAP.analyzer.views import runMAPValueGraph, runMAPBenchmarkGraph
from .MRR.analyzer.views import runMRRValueGraph, runMRRBenchmarkGraph
#from .NDCG.analyzer.views import runMAPGraph

def runEvaluations(limit=5):
    runMAP(limit=limit)
    runMRR(limit=limit)
    runNDCG(limit=limit)

def runValueAnalizer():
    runMAPValueGraph()
    runMRRValueGraph()

def runBenchAnalizer():
    runMAPBenchmarkGraph()
    runMRRBenchmarkGraph()
