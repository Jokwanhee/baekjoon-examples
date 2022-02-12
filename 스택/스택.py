'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


********************************************************************************
함수로 작성해서 시간초과...
input("")으로 작성해서 시간초과...
=> sys.stdin.readline() 으로 진행해야 한다...
********************************************************************************
'''
import sys

items = []

C = int(input(""))

for i in range(C):
    user = tuple(map(str, sys.stdin.readline().split()))
    if user[0] == "push":
        items.append(int(user[1]))
    elif user[0] == "pop":
        if len(items) == 0:
            print(-1)
        else:
            print(items.pop(-1))
    elif user[0] == "empty":
        if len(items) == 0:
            print(1)
        else:
            print(0)
    elif user[0] == "size":
        print(len(items))
    elif user[0] == "top":
        if len(items) == 0:
            print(-1)
        else:
            print(items[-1])
