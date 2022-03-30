import sys
from collections import deque

N = int(sys.stdin.readline())
result = deque()
end = 0
if N == 1:
    pass
elif N in (2,3,5,7):
    print(N)
else:
    while True:
        for n in range(2, N+1):
            if N % n == 0:
                print(n)
                N = N // n
                if N == 1:
                    end = -1
                break
        if end == -1:
            break
