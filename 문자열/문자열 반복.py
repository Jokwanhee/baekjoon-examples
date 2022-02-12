'''
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
'''
import sys

T = int(input(""))

for i in range(T):
    checkPoint = 0
    S = list(map(str, sys.stdin.readline().split()))
    R = int(S[0])
    list_S = list(S[1])
    for j in list_S:
        if j in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:":
            pass
        else:
            checkPoint = -1
            break
    if checkPoint == -1:
        break
    for j in range(len(list_S)):
        list_S[j] = list_S[j] * R
    list_S = "".join(list_S)
    print(list_S)