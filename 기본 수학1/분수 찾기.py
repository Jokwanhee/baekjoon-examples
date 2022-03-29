import sys

X = int(sys.stdin.readline())

n = 0
while True:
    n += 1
    a = (n*(n-1)) / 2
    b = (n*(n+1)) / 2
    if a < X <= b:
        if n % 2: # 홀수
            high = b - X + 1
            low = X - a
            result = str(int(high)) + "/" + str(int(low))
            break
        else: # 짝수
            high = X - a
            low = b - X + 1
            result = str(int(high)) + "/" + str(int(low))
            break
print(result)