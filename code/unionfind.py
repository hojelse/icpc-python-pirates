class uf:
  def __init__(self, n): 
    self.p = [-1]*n
  def find(self, v): 
    u = v
    while self.p[v] >= 0:
      self.p[u], v, u = self.p[v], self.p[v], v
    return v
  def union(self, u, v):
    u, v = self.find(u), self.find(v)
    if u != v:
      if self.p[u] > self.p[v]: u, v = v, u
      self.p[u], self.p[v] = self.p[u]+self.p[v], u