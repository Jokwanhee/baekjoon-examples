import sys
from collections import deque

N = int(sys.stdin.readline())
D = deque()
result = 0

for n in range(1, N + 1):
    D.append(n)

if len(D) == 1:
    result = 1
else:
    for i in range(len(D)):
        D.popleft()
        D.rotate(-1)
        if len(D) == 1:
            result = D[0]
            break

print(result)