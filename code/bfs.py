def bfs(g, s):
  seen = set()
  q = deque([s])
  while q:
    u = q.pop()
    for v in g[v]:
      if v not in seen:
        seen.add(v)
        q.appendleft(v)