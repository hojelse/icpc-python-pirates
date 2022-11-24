# depends on union-find
from heapq import heappush, heappop, heapify
def kruskal(G, n):
  C, mst, W = uf(n), [], 0
  E = [(w,u,v) for u,es in G.items() for v,w in es.items()]
  heapify(E)

  while E and len(mst) < n-1:
    w,u,v = heappop(E)
    if C.find(u) != C.find(v):
      C.union(u,v)
      mst.append((u,v))
      W += w

  if C.c > 1: return None, None
  return (mst), W
