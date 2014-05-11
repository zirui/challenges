import sys
import math

def solve(N, C, M):
    ans = N*M/(C*(M-1)) 
    return ans

def main():
    T = int(raw_input())
    for i in (0,T,1):
        line = raw_input()
        N, C, M = [int(val) for val in line.strip().split()]
        #print N, C, M 
        ans = solve(N, C, M)
        print ans

if __name__ == '__main__':
    main()
