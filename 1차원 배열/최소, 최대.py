'''
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
'''

try:
    N = int(input(""))
    n_list = list(map(int, input("").split()))
    if N == len(n_list):
        n_min = n_list[0]
        n_max = n_list[0]
        for i in n_list:
            if n_max <= i:
                n_max = i
            if n_min >= i:
                n_min = i
        print(n_min, n_max)
except:
    exit()
