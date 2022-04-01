import sys

listX = []
listY = []
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    listX.append(x)
    listY.append(y)

for x in set(listX):
    if listX.count(x) == 1:
        print(x, end=" ")
for y in set(listY):
    if listY.count(y) == 1:
        print(y)
