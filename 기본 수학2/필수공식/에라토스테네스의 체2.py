def isPrime(num):
    if num == 1:
        return False
    else:
        for n in range(2,int(num**0.5)+1):
            if num % n == 0:
                return False
        return True


M = 100
mine = []

for m in range(2,M+1):
    if isPrime(m):
        mine.append(m)

print(mine)
