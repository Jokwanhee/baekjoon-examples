'''
힌트
우선 주어진 최댓값의 소수를 구하여 리스트로 정리한다.
만약 해당 소수를 while문에서 계속 에라토스테네의 체를 사용하여 구하면
오래걸릴 수 있다.
'''


import sys

def isPrime(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                return False
        return True

M = 123456
allNum = [x for x in range((2*M) + 1)]
myNum = []

for a in allNum:
    if a != 0:
        if isPrime(a):
            myNum.append(a)

while True:
    N = int(sys.stdin.readline())
    multipleN = 2*N
    if N == 0:
        break
    else:
        cnt = 0
        for mine in myNum:
            if N < mine <= multipleN:
                cnt += 1
        print(cnt)