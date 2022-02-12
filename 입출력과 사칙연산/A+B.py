# 두 개의 변수를 input 받는 방법
A, B = input("").split()

A = int(A)
B = int(B)

if A > 0 and B < 10:
    result = A + B
    print(result)
