import sys

A = list(map(int, sys.stdin.readline().split()))
result = 0
for a in A:
    result += a
print(result)