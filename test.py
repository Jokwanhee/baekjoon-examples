for n in range(1,100):
    if n == 1:
        continue
    for i in range(2,10):
        if n % i == 0:
            break
    else:
        print(n)
