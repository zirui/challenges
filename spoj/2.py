import sys
import math
#import psyco

case_num = input()


for k in xrange(0,case_num):
    m,n = sys.stdin.readline().strip().split()
    m = int(m)
    n = int(n)
    primes = [True] * (n-m+1) 
    sqrtn = int(math.sqrt(n))
    for i in xrange(2,sqrtn+1,1):
        start = m/i * i
        for j in xrange(start ,n+1,i):
            if j != i and j >= m:
                primes[j-m] = False

    for i in xrange(len(primes)):
        if primes[i] and (i+m) != 1:
            print i+m
    print ''


