def eugcd(a,b):
  return eugcd(b,a%b) if b > 0 else a