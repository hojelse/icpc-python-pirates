def fold(it, acc, folder):
  for i in it: acc = folder(acc, i)
  return acc

def issorted(xs):
  if len(xs) > 1: 
    for i in range(1, len(xs)):
      if xs[i-1] > xs[i]:
        return False
  return True

def runs(xs):
  def folder(rs, x):
    if rs[-1][0] >= rs[-1][-1] >= x:
      rs[-1].append(x)
    else:
      rs.append([x])
    return rs
  return fold(xs[2:], [xs[0:2]], folder)

def runs_overlapping(xs):
  def folder(rs, x):
    if rs[-1][0] >  rs[-1][-1] >  x \
    or rs[-1][0] <  rs[-1][-1] <  x \
    or rs[-1][0] == rs[-1][-1] == x:
      rs[-1].append(x)
    else:
      rs.append([rs[-1][-1], x])
    return rs
  return fold(xs[2:], [xs[0:2]], folder)

def fuse(xs):
  def folder(xs, r):
    if xs[-1] == r[0]: xs.pop()
    xs.extend(r)
    return xs
  return fold(xs[1:], [xs[0]], folder)