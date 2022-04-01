import sys

x, y, w, h = map(int, sys.stdin.readline().split())

distanceX = w - x
distanceY = h - y
resultX, resultY = 0, 0
if distanceX < x:
    resultX = distanceX
else: resultX = x
if distanceY < y:
    resultY = distanceY
else: resultY = y

result = 0
if resultX < resultY:
    result = resultX
else: result = resultY

print(result)
