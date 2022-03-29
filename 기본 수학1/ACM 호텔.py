import sys

T = int(sys.stdin.readline())

for t in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    first = (N % H)*100
    if N % H == 0:
        first = H * 100
    end = (N - 1) // H + 1
    result = first + end
    print(result)