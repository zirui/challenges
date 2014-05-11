


def solution(A):
    n = len(A)
    left_min = [0] * n
    right_max = [0] * n
    left_min[0] = A[0]
    for i in xrange(1,n):
        left_min[i] = min(left_min[i-1],A[i])
    right_max[n-1] = A[n-1]
    for i in xrange(n-2,-1,-1):
        right_max[i] = max(right_max[i+1],A[i])
        
    i , j, max_diff = 0,0,0
    while i < n and j < n:
        if left_min[i] <= right_max[j]:
            max_diff = max(max_diff, j - i)
            j += 1
        else:
            i += 1
    return max_diff


def solution2(A):
    n = len(A)
    dec = [0]
    for i in xrange(1,n):
        if A[i] <= A[dec[-1]]:
            dec.append(i)
    i, j, max_diff = len(dec)-1, n-1, 0
    while  i >= 0:
        if A[j] >= A[dec[i]]:
            max_diff = max(max_diff, j - dec[i])
            i -= 1
        else:
            j -= 1
    return max_diff


def solution3(A):
    dec = []
    max_diff = 0
    for i in xrange(len(A)-1,-1,-1):
        print i, dec
        while len(dec) > 0 and A[i] >= A[dec[-1]]:
            max_diff = max(max_diff, i - dec[-1])
            dec.pop()
        dec.append(i)
    return max_diff



A = [5,3,6,3,4,2]
print solution2(A)
