'''
크기가 N인 수열 A = A1, A2, ..., AN이 있다.
수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
그러한 수가 없는 경우에 오큰수는 -1이다.
예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다.
A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

풀이 방법
1. 오큰수를 나타내는 [-1]*N 리스트 생성
2. stack 사용 -> 검사 대상

예를 들어서, 3 5 2 7 존재
처음 stack에는 아무것도 들어있지 않아서 while 반복문 사용 x
stack 3과 그에 해당하는 인덱스 0을 삽입
다음 들어올 5와 stack[-1][0]을 비교 (5 > 3)
들어온 것이 크다면 stack pop => 오큰수에 pop 한 값의 인덱스를 넣어 오큰수 변경

[참고]
https://hooongs.tistory.com/329
'''
import sys
from collections import deque

A = int(sys.stdin.readline())

items = list(map(int, sys.stdin.readline().split()))
NGE = [-1]*A
stack = deque()
for a in range(A):
    while stack and (stack[-1][0] < items[a]):
        val, idx = stack.pop()
        NGE[idx] = items[a]
    stack.append([items[a],a])

print(*NGE)

