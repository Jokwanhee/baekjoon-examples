N, X = map(int, input("").split())

N_list = list(map(int, input("").split()))
if len(N_list) == N:
    for i in N_list:
        if i < X:
            print(i, end=" ")