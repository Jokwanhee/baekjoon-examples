import sys

def isTriangle(a,b,c):
    if a*a + b*b == c * c: return True
    return False

while True:
    triangleList = list(map(int, sys.stdin.readline().split()))
    if triangleList[0] == 0 or triangleList[1] == 0 or triangleList[2] == 0:
        break
    else:
        c = max(triangleList)
        idx = []
        for t in range(len(triangleList)):
            if t != triangleList.index(c):
                idx.append(t)
        a = triangleList[idx[0]]
        b = triangleList[idx[1]]
        if isTriangle(a,b,c):
            print("right")
        else:
            print("wrong")