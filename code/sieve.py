from math import ceil,sqrt
def sieve(n):
    if n < 2: return [], 0
    if n <= 2: return [1], 1
    if n <= 3: return [1,0], 1
    rn, n = int(ceil(sqrt(n))), int(ceil(n/2.0))
    c, i = n, 2
    S = [0]*(n+1) # can replace with bitvec
    S[0], S[1] = 1, 0
    for j in range(4, n, 3): S[j], c = 1, c-1
    while i < rn//2:
      while S[i]: i+= 1
      k = (i << 1) | 1
      for j in range(i+2*k, n, 3*k):
        if not S[j]: S[j], c = 1, c-1
      for j in range(i+3*k, n, 3*k):
        if not S[j]: S[j], c = 1, c-1
      i += 1
    return S, c
# if S[i//2]=0 then prime(i)=True for i%1=1