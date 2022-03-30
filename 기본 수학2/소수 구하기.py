'''
힌트
M ~ N 사이의 소수를 구할 수 있어야 한다.
ex) 1 ~ 20
각 수의 약수
10 : 1, 2, 5, 10
10의 제곱근 : 3.1~
2,3 의 수 중 10과 나눠진다면 이 수는 소수가 아니다
11 의 제곱근 : 3.3~
2,3 의 수 중 11과 나눠지는 수가 없다 그러므로 소수
'''

import sys

M, N = map(int, sys.stdin.readline().split())
for n in range(M,N+1):
    if n == 1:
        continue
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        print(n)