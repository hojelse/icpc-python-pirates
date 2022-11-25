import sys
sys.setrecursionlimit(10**6)
def dfs(g, s, seen):
  if s not in seen:
    seen.add(s)
    for v in g[s]:
      if v not in seen:
        dfs(g,v,seen)