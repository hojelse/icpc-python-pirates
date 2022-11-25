from functools import lru_cache
@lru_cache
def lcs(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    return max(
      lcs(s1[:-1], s2), lcs(s1, s2[:-1]), 
      (s1[-1] == s2[-1]) + lcs(s1[:-1], s2[:-1])
    )