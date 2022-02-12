N = int(input(""))

for i in range(N - 1, -1, -1):
    for j in range(N):
        if j >= i:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
