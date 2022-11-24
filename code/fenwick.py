F = [0]*(n+1)
def prefix(F, i): # 1-indexed i
    if i > 0: 
        return F[i] + pre(F, i - (i & -i))
    return 0
def add(F, i, delta): # 1-indexed i
    if i < len(F): 
        F[i] += delta
        add(F, i + (i & -i), delta)