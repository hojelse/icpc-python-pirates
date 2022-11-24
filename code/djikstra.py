from heapq import heappush, heappop
def djikstra(g,s):
  dead = set()
  dist = defaultdict(constant(inf))
  path = defaultdict(constant(None))
  pq, dist[s] = [(0,s)], 0
  while pq:
    distu, u = heappop(pq)
    if u in dead: continue 
    dead.add(u)
    for v,w in g[u].items():
      if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        path[v] = u
        heappush(pq, (dist[u]+w, v))
  return dist, path