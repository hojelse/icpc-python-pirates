## Ford Fulkerson with scaling
INF = 2**31-1
def ffdfs(g, s, t, seen, f, t):
  if s == t:
    return f
  if s not in seen:
    seen.add(s)
    for nxt,cap in g[s].items():
      if cap >= t:
        delta = fdfs(g, nxt, t, seen, min(f, cap), t)
        if delta >= t:
          g[s][nxt] -= delta
          g[nxt][s] += delta
          return delta
  return 0

def fordFulkersonScaling(g, s, t, init_t):
  f = 0
  t = init_t

  while t > 0: 
    delta = INF
    while delta > 0:
      delta = fdfs(g, s, t, set(), INF, t)
      f += delta
    t = t//2

  return f

## Dinic's
def dfdfs(g, s, t, l, f, seen):
  if s == t:
    return f
  if s not in seen:
    seen.add(s)
    for nxt,cap in g[s].items():
      if cap >= 1 and s in l and nxt in l and l[s] < l[nxt]:
        delta = dfdfs(g, nxt, t, l, min(f, cap), seen)
        if delta >= 1:
          g[s][nxt] -= delta
          g[nxt][s] += delta
          return delta
  return 0

def lvlbfs(g, s, t):
  l = {s:0}
  q = deque([(s,0)])
  while q:
    v,vl = q.pop()
    if v == t: 
      l[v] = vl + 1
      break
    for w,c in g[v].items():
      if w in l or c == 0: continue 
      l[w] = vl + 1
      q.appendleft((w, vl + 1))
  return l

def dinics(G, s, t, f=0):
  levels = lvlbfs(G, s, t)
  if t not in levels: return f

  increase = inf
  while increase > 0:
    increase = dfdfs(G,s,t,levels,inf,set())
    f += increase

  return dinics(G, s, t, f=f)
