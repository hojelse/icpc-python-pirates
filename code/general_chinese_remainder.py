def gcd(a,b):
  while b > 0: a, b = b, a%b
  return a

def lcm(a,b): 
  return (a*b)//gcd(a,b)

def bezout_id(a, b):
    r,x,s,y,t,z = b,a,0,1,1,0
    while r:
        q = x // r
        x, r = r, x % r
        y, s = s, y - q * s
        z, t = t, z - q * t
    return y % (b // x), z % (-a // x)

def general_chinese_remainder(a,b,m,n):
  g = gcd(m,n)

  if a == b and m == n:
    return a, m
  if (a % g) != (b % g): 
    return None, None

  u,v = bezout_id(m,n)
  x = (a*v*n + b*u*m) // g
  return int(x) % lcm(m,n), int(lcm(m,n))