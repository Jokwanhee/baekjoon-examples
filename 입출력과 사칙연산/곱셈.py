first_line = int(input(""))
second_line = input("")

for i in second_line[::-1]:
    i = int(i)
    print(first_line * i)

second_line = int(second_line)
print(first_line * second_line)
