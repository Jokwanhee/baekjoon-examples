'''
    # 반례
    우선순위 : 2 1 2 1 2
    1) 5 2 => 2
    2) 5 3 => 3
    3) 5 4 => 5
    우선순위 : 1 9 1 9 1 9
    1) 6 3 => 2
'''

import sys
from collections import deque

T = int(sys.stdin.readline())

for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    priority = deque(map(int, sys.stdin.readline().split()))
    findNum = priority[M]
    priority[M] = 0
    result = []
    if len(priority) == 1:
        result.append(0)
    else:
        while True:
            MAX_ITEM = max(priority)
            d = priority.popleft()
            if d == 0 and findNum < MAX_ITEM:
                priority.append(d)
            elif d == 0 and findNum >= MAX_ITEM:
                result.append(d)
                break
            else:
                if d == MAX_ITEM and findNum <= MAX_ITEM:
                    result.append(d)
                elif d == MAX_ITEM and findNum > MAX_ITEM:
                    priority.append(d)
                elif d < MAX_ITEM:
                    priority.append(d)

    print(result.index(0) + 1)