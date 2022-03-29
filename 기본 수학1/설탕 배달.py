'''
힌트
뒷자리
1,2,3,4,5,6,7,8,9,0 의 값들이 어떠한 규칙을 갖는 지 확인 후 계산
ex)
3,6,9
3 : 3*1, 13 : 5*2 + 3*1
6 : 3*2, 16 : 5*2 + 3*2
1
1 : x, 11 : 5*1 + 3*2, 21 : 5*3 + 3*2
와 같은 규칙 찾기
'''

import sys
import math

N = int(sys.stdin.readline())
digit = math.pow(10, len(str(N)) - 1)

first = int(list(str(N))[0])
end = int(list(str(N))[-1])

cnt = 0
if end == 3 or end == 6 or end == 9:
    if digit == 1: cnt = end // 3
    else: cnt = (N - end) // 5 + end // 3
elif end == 0 or end == 5:
    if N == 0: cnt = -1
    else: cnt = N // 5
elif end == 1:
    if digit == 1: cnt = -1
    else: cnt = (N - 6) // 5 + 2
elif end == 2 or end == 7:
    if digit == 1: cnt = -1
    else: cnt = (N - 12) // 5 + 4
elif end == 4:
    if digit == 1: cnt = -1
    else: cnt = (N - 9) // 5 + 3
elif end == 8:
    cnt = (N - 3) // 5 + 1
print(cnt)
