hours, minutes = input("").split()

hours = int(hours)
minutes = int(minutes)

if (hours >= 0 and hours <= 23) and (minutes >= 0 and minutes <= 59):
    result = minutes - 45
    if result < 0:
        hours -= 1
        result = 60 + result
        if hours < 0:
            hours = 23
        print(hours, result, end=" ")
    else:
        print(hours, result, end=" ")
