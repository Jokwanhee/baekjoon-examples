n = int(input(""))

if n >= 1 and n <= 10_000:
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)