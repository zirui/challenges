import sys

line = sys.stdin.readline()
a, b = line.strip().split()
ans = int(a) ^ int(b)
print ans
