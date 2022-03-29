'''
     1호  2호  3호  4호
3층 - 1   5   15    35
2층 - 1   4   10    20
1층 - 1   3   6     10
0층 - 1   2   3     4
'''

import sys

T = int(sys.stdin.readline())


for t in range(T):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    result = 0
    floor = [n for n in range(1,N+1)]
    for k in range(K):
        for n in range(1, N):
            floor[n] += floor[n-1]
    print(floor[-1])

