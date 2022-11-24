
# Graph representation: nested dict
# weighted => use values for weights
# unweighted => use dummy values
# same repr, same code, same algorithms
# also easily represent dir/undir

unweighted = ['0 1','0 2','0 3','1 2','1 3','2 3']
weighted = ['0 1 1','0 2 1','0 3 0','1 2 3','1 3 3']

from collections import defaultdict
G = defaultdict(dict)
for line in unweighted:
  u,v,w = map(int, line.split())
  G[u][v] = G[v][u] = True

G = defaultdict(dict)
for line in weighted:
  u,v,w = map(int, line.split())

  G[u][v] = G[v][u] = w

# String builder pattern, very useful for outputting fast
output = []
for i in range(10**6): output.append(str(i))
print('\n'.join(output))

# Heaps
from heapq import heappop, heappush
h = []
heappush(h, (1,'hello'))
minprio, thing = heappop(h)

