import sys

try:
    N = sys.stdin.readline().rstrip()
    base_N = N
    if len(base_N) == 1:
        base_N = "0" + base_N
    re_N = ""
    count = 0
    while True:
        if int(N) == 0:
            count = 1
            break
        if int(N):
            count += 1
            if len(N) == 1:
                N = "0" + N
            number = int(N) % 10
            result = int(N) % 10 + int(N) // 10
            re_N = str(number) + str(result % 10)
            if base_N == re_N:
                break
            else:
                N = re_N
    print(count)
except:
    exit()
