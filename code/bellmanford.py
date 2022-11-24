from collections import defaultdict
from math import inf

def edges(g):
    return [(u,v,w) for u,es in g.items() for v,w in es.items()]

def constant(val): return lambda: val
def bellmanford(g,s,n):
    dist = defaultdict(constant(inf))
    path = defaultdict(constant(None))
    dist[s] = 0
    for i in range(n-1):
        for u,v,w in edges(g):
            if dist[u] + w < dist[v]:
                dist[v], path[v] = dist[u] + w, u

    return dist, path