import sys
from collections import deque

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

result = deque()
decimalSum = 0
for idx in range(M,N+1):
    cnt = 0
    for i in range(1,idx+1):
        if idx % i == 0:
            cnt += 1
            if cnt > 2:
                break
    if cnt == 2:
        result.append(idx)
        decimalSum += idx

if len(result) == 0:
    print(-1)
else:
    print(decimalSum)
    print(result[0])