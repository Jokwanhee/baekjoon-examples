import sys
from collections import deque

T = int(sys.stdin.readline())

for t in range(T):
    P = [i for i in sys.stdin.readline().rstrip()]
    N = int(sys.stdin.readline())
    nList = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    result = ""
    rev = 0
    flag = 0
    if N == 0:
        nList = []
    for p in P:
        if p == "R":
            rev += 1
        elif p == "D":
            if len(nList) < 1:
                result = "error"
                flag = 1
                break
            else:
                if rev % 2:
                    nList.pop()
                else:
                    nList.popleft()
    if flag == 0:
        if rev % 2:
            nList.reverse()
        result += "[" + ",".join(nList) + "]"
    print(result)
