'''
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
an = a1 + (n-1)d / a1: 첫째 항, d: 공차
ex) 101 --> 99
101 보다 작은 수 1~100 중 등차수열인 수의 개수를 구하는 것
1 -> 첫 항 : 1, 공차 : 0
11 -> 첫 항 :1, 둘째 항 : 1, 공차 : 0
요런식!
'''

N = int(input(""))

a1 = 0
d = 0
count = 0
for i in range(1, N + 1):
    isHansu = 1
    str_N = str(i)
    list_N = list(str_N)
    for i in range(len(list_N)):
        list_N[i] = int(list_N[i])
    if len(list_N) == 1:
        a1 = list_N[0]
        count += 1
    elif len(list_N) == 2:
        a1 = list_N[0]
        d = list_N[1] - a1
        count += 1
    else:
        a1 = list_N[0]
        d = list_N[1] - a1
        for i in range(len(list_N) - 1, 0, -1):
            if d == list_N[i] - list_N[i - 1]:
                isHansu += 1
            if isHansu == len(list_N):
                count += 1

print(count)