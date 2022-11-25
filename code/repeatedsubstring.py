import random
import sys

p = 6864654970276223
a = random.randint(1, 2**8)  

def repeated_string(x, m): # -> True if x has a 
                           #repeated substring of length m
    global a

    found = set() # all the hashcodes we have seen
    h = 0
    # compute A^m
    multiplier = 1

    # compute hash of x[0],..., x[m - 1]
    for i in range(m):
        h = (h * a + ord(x[i])) % p
        multiplier = (multiplier * a) % p

    found.add(h)

    # rolling hash over remaining string
    for i in range(1, n - m):
        # remove first coefficent a^{m - 1}x[i - 1] from h
        h = (a * h - ord(x[i-1]) * multiplier) %p
        h = (h + ord(x[i + m - 1])) %p

        if h in found:
            return True
        found.add(h)
    return False