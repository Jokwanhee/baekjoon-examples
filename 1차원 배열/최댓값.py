'''
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
'''
import sys

try:
    n_list = []
    while True:
        n = int(sys.stdin.readline().rstrip())
        n_list.append(n)
        if len(n_list) == 9:
            break
    n = n_list[0]
    count = 0
    for i in n_list:
        if n <= i:
            n = i
            count = n_list.index(i) + 1
    print(n, count)
except:
    exit()

