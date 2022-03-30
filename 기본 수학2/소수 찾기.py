import sys
from collections import deque

N = int(sys.stdin.readline())

items = list(map(int, sys.stdin.readline().split()))
result = deque()
for item in items:
    cnt = 0
    for i in range(1,item+1):
        if item % i == 0:
           cnt += 1
    if cnt == 2:
        result.append(item)
print(len(result))
