T = int(input(""))

for i in range(T):
    a, b = input("").split()
    a = int(a)
    b = int(b)
    if a > 0 and b < 10:
        print(a + b)