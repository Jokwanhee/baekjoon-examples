a = []
for i in range(10000):
    result = 0
    for j in list(str(i)):
        j = int(j)
        result += j
    result += i
    a.append(result)

a.sort()

b = []
for i in range(10000):
    if i in a:
        continue
    else:
        b.append(i)

b.sort()
for i in b:
    print(i)
