def vec(a,b):
    return (b[0]-a[0],b[1]-a[1])
def det(a,b):
    return a[0]*b[1] - b[0]*a[1]

def convexhull(P):
    if (len(P) == 1):
        return [(p[0][0], p[0][1])]

    h = sorted(P)
    lower = []
    i = 0
    while i < len(h):
        if len(lower) > 1:
            a = vec(lower[-2], lower[-1])
            b = vec(lower[-1], h[i])
            if det(a,b) <= 0 and len(lower) > 1:
                lower.pop()
                continue
        lower.append(h[i])
        i += 1

    upper = []
    i = 0
    while i < len(h):
        if len(upper) > 1:
            a = vec(upper[-2], upper[-1])
            b = vec(upper[-1], h[i])
            if det(a,b) >= 0:
                upper.pop()
                continue
        upper.append(h[i])
        i += 1

    reversedupper = list(reversed(upper[1:-1:]))
    reversedupper.extend(lower)
    return reversedupper