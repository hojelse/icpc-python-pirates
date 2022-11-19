# Slicing
L = '0123456789'
L[5]        # '5'           ith element of L
L[2:6]      # '2345'        range [i; j[
L[:6]       # '012345'      range [0; j[
L[2:]       # '23456789'    range [i; N[
L[-2:]      # '89'          range [N-2; N[
L[0:10:2]   # '02468'       range [i; j[ with s sized steps
L[::2]      # '02468'       evens
L[:]        # '0123456789'  copy
L[::-1]     # '9876543210'  reverse copy

# Sorting
sorted([2,1,3,4])                      # [1,2,3,4]
sorted([2,1,3,4], reverse=True)        # [4,3,2,1]
sorted([2,1,3,4], key=lambda x: x%2)   # [2,4,1,3]
[2,1,3,4].sort()                       # void (sorted in-place)

# List operations
L = 'foo bar baz'
len(L)              # num items           O(1)
sorted(L)           # sort                O(n log n)
L.count('ba')       # num of occurences   O(n)
'bar' in L          # contains            O(n)

L = []
L.append('first')   # push                amortised O(1)
L.pop()             # pop                 amortised O(1)

# List comprehension
[x for x in range(10)]                     # [0,1,2,3,4,5,6,7,8,9]
[(4**x)//3 for x in range(1,7)]            # [1,5,21,85,341,1365]
{k:v for (k,v) in [('a',1), ('b',2)]}      # {'a': 1, 'b': 2}
[(k,v) for k,v in {'a':1, 'b':2}.items()]  # [('a', 1), ('b', 2)]
[0]*5                                      # [0, 0, 0, 0, 0]

# Matrix transposition
tuple(zip(*((1,2), (3,4))))             # ((1,3), (2,4))
list(map(list, zip(*[[1,2], [3,4]])))   # [[1,3], [2,4]]

# Substring search
"foo bar baz".find("bar")          # 4
"foo bar baz".find("bar", 0, 5)    # -1
"foo bar baz".index("bar")         # 4
"foo bar baz".index("bar", 0, 5)   # substring not found
"foo bar baz".startswith("foo")    # True
"foo bar baz".endswith("baz")      # True
"foo bar baz".count("ba")          # 2
"foo bar baz".count("barz")        # 0

# String format and interpolation
x = 12.005
f"Interpolated: {x}"       # 'Interpolated: 12.005'
f"Two decimals: {x:.2f}"   # 'Two decimals: 12.01'

# IO
input()                        # slow read line
import sys                     # fast read line
sys.stdin.readline().strip()
import os                      # fast read all bytes
os.read(0, 100).split()

# collections
import collections
d = collections.defaultdict(int)   # dict with default value
l = collections.deque()            # double ended queue/stack

# interation and enumeration with for x in iterable
iter('abc')                     # 'a' 'b' 'c' ...
enumerate('abc')                # (0,'a') (1,'b') (2,'c') ...
{'a':0, 'b':1, 'c':2}.items()   # ('a', 0) ('b', 1) ('c', 2) ...

# itertools
import itertools
itertools.count(10)                 # 10 11 12 13 14 ...
itertools.count(10, 2)              # 10 12 14 16 18 ...
itertools.cycle('ABC')              # A B C A B C ...
itertools.permutations(range(3))    # 012 021 102 120 201 210
itertools.permutations('ABCD', 2)   # AB AC AD BA BC BD CA CB CD DA DB DC
itertools.combinations('ABCD', 2)   # AB AC AD BC BD CD

# Strings
import string
string.ascii_uppercase   # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_lowercase   # 'abcdefghijklmnopqrstuvwxyz'
string.ascii_letters     # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits            # '0123456789'
string.punctuation       # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
string.whitespace        # ' \t\n\r\x0b\x0c'

# String cases
"all lower case".lower()          # 'all lower case'
"all caps".upper()                # 'ALL CAPS'
"first upper case".capitalize()   # 'First upper case'
"title case".title()              # 'Title Case'
"Reverse Case".swapcase()         # 'rEVERSE cASE'
"is lower case?".islower()        # True
"IS UPPER CASE?".isupper()        # True
"Is Title Case?".istitle()        # True
"abcXYZ012".isalnum()             # True
"abcXYZ".isalpha()                # True
"0123".isdecimal()                # True
" \t\n\r\x0b\x0c".isspace()       # True

# Base conversion and encoding
chr(65)                 # 'A'
hex(65)                 # '0x41'
oct(65)                 # '0b101'
bin(65)                 # '0b1000001'
ord('A')                # 65
0x41                    # 65
0b1000001               # 65
'\x41\x42\x43'          # 'ABC'

'\x41'.encode('UTF-8')            # b'A'
b'A'.decode('UTF-8', 'strict')    # 'A'
