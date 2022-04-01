'''
두 원의 교점을 구할 수 있어야 한다.
A : x1^2 + y1^2 + ax1 + by1 + c = 0
B : x2^2 + y2^2 + a'x2 + b'y2 + c' = 0
두 원을 지나는 직선의 방정식
(a-a')x + (b-b')y + c - c' = 0
'''
import sys

x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

a1 = -2*x1
b1 = -2*y1
c1 = -(r1*r1) + x1*x1

a2 = -2*x2
b2 = -2*y2
c2 = -(r2*r2) + x2*x2