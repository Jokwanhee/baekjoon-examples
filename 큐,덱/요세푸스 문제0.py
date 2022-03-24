import sys

N, K = map(int, sys.stdin.readline().split())

resultList = []
NList = []

for n in range(1,N+1):
    NList.append(n)

cnt = 1
n = 0
while len(resultList) != N:
    idx = n % N
    if NList[idx] != 0:
        if (cnt % K) == 0:
            resultList.append(NList[idx])
            NList[idx] = 0
        cnt += 1
    n += 1

result = "<"
for r in resultList:
    result += str(r) + ", "
result = result[:-2] + ">"
print(result)