import sys
from collections import deque

N = int(sys.stdin.readline())

items = deque()
for n in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        items.appendleft(command[1])
    elif command[0] == "push_back":
        items.append(command[1])
    elif command[0] == "pop_front":
        if len(items) == 0: print(-1)
        else:
            d_front = items.popleft()
            print(d_front)
    elif command[0] == "pop_back":
        if len(items) == 0: print(-1)
        else:
            d_back = items.pop()
            print(d_back)
    elif command[0] == "size":
        size = len(items)
        print(size)
    elif command[0] == "empty":
        if len(items) == 0: print(1)
        else: print(0)
    elif command[0] == "front":
        if len(items) == 0: print(-1)
        else: print(items[0])
    elif command[0] == "back":
        if len(items) == 0: print(-1)
        else: print(items[-1])