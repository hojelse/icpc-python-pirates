from array import array as arr
from math import ceil
class bitvector:
    def __init__(self, n):
        self._ = arr('B',(0 for i in range(int(ceil(n/8)))))
    def __getitem__(self, i):
        return self._[i//8] & (1<<(i%8))
    def __setitem__(self, i, v):
        self._[i//8] |= (v<<(i%8))