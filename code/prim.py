from heapq import heappush, heappop, heapify
def prim(G, n):
  s = next(iter(G.keys()))
  V = set([s])
  M = []
  c = 0

  E = [(w,s,v) for v,w in G[s].items()]
  heapify(E)

  while E and len(M) < n-1:
    w,u,v = heappop(E)
    if v in V: continue
    V.add(v)
    M.append((u,v))
    c += w
    u = v
    [heappush(E,(w,u,v)) for v,w in G[u].items() if v not in V]

  if len(M) == n-1:
    return M, c
  else:
    return None, None