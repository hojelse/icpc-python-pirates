from io import BytesIO
from sys import stdin, stdout
from atexit import register

# <PREAMBLE>
buffer = BytesIO()
stdout = buffer
@register
def write(): stdout.write(buffer.getvalue())
# </PREAMBLE>
# input: stdin.readline()
# output: print(whatever)