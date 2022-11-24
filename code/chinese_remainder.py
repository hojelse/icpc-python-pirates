# Modular inverse of a modulo b
def modinv(a, b):
  if b == 1: return 1
  b0, x0, x1 = b, 0, 1
  while a > 1:
    q, a, b = a//b, b, a%b
    x0, x1 = x1 - q * x0, x0
  if x1 < 0: x1 += b0
  return x1

# an x such that forall y,m: yx = 1 mod m
# requires all m,m' to be >=1 and coprime
def chinese_remainder(ys, ms):
  N, x = 1, 0
  for m in ms: N*=m
  for y,m in zip(ys,ms):
    n = N // m
    x += n * y * modinv(n, m)
  return x % N