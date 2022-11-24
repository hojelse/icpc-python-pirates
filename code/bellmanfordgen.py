from collections import defaultdict
from sys import setrecursionlimit
from math import inf
setrecursionlimit(10**6)

def edges(g):
    return [(u,v,w) for u,es in g.items() for v,w in es.items()]

def dfs_mark(g,u,seen,dist):
    if u not in seen:
        seen.add(u)
        dist[u] = -inf
        for v in g[u]:
            dfs_mark(g,v,seen,dist)

def constant(val): return lambda: val
def bellmanford(g,s,n):
    dist = defaultdict(constant(inf))
    path = defaultdict(constant(None))
    dist[s] = 0
    for i in range(n-1):
        for u,v,ws in edges(g):
            for w in ws:
                if dist[u] + w < dist[v]:
                    dist[v], path[v] = dist[u] + w, u

    # negative cycle support, -inf for arbitrary short
    seen = set()
    for u,v,ws in edges(g):
        for w in ws:
            if dist[u] + w < dist[v]:
                dfs_mark(g,v,seen,dist)

    return dist, path