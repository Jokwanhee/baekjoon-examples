import sys

T = int(input(""))

for i in map(lambda x: x, range(1, T + 1)):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i, A, B, A + B))
