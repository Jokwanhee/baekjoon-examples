x = int(input(""))
y = int(input(""))

if (x >= -1_000 and x <= 1_000 and x != 0) and (y >= -1_000 and y <= 1_000 and y != 0):
    if x > 0 and y > 0:  # 1사분면
        print("1")
    elif x < 0 and y > 0:  # 2사분면
        print("2")
    elif x < 0 and y < 0:  # 3사분면
        print("3")
    elif x > 0 and y < 0:  # 4사분면
        print("4")
