import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

order = list(map(int, sys.stdin.readline().split()))

component = deque([n for n in range(1, N+1)])
result = 0
for item in order:
    while True:
        idx = component.index(item)  # 원하는 값의 위치
        S = len(component) // 2  # 전체 크기를 2로 나누어 b와 c 연산을 구분하기위한 기준
        if idx == 0: # 원하는 값의 위치가 맨 앞이면 a 연산 : ex) item = 2, 2 3 4 5 6 => 2 삭제
            component.popleft()
            break
        else:
            if idx <= S:
                component.rotate(-1)
                result += 1
            else:
                component.rotate(1)
                result += 1

print(result)