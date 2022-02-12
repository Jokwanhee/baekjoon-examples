score = int(input(""))

if score >= 0 and score <= 100:
    if score < 60:
        print("F")
    elif score <= 69:
        print("D")
    elif score <= 79:
        print("C")
    elif score <= 89:
        print("B")
    elif score <= 100:
        print("A")


