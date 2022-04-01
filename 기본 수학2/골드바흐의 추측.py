import sys


def isPrime(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True


M = 10000
listM = [i for i in range(M + 1)]
items = []

for m in range(1, M + 1):
    if isPrime(m):
        items.append(m)

T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    for item in items:
        if n // 2 <= item <= n:
            if n - item in items:
                print(n-item, item)
                break
