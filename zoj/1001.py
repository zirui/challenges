import sys


for line in sys.stdin:
    a, b = line.split()
    ans = int(a) + int(b)
    print ans
