'''
V : 나무 높이
A : 달팽이가 낮 동안 나무를 오르는 거리
B : 달팽이가 밤 동안 자면서 나무에서 미끄러지는 거리
'''
import math
import sys

A, B, V = map(int, sys.stdin.readline().split())
result = (V - A) / (A - B)
result = math.ceil(result) + 1
print(result)


