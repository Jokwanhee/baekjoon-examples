import sys

INPUT = int(sys.stdin.readline())

items = []
cnt = 0

for i in range(INPUT):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        items.append(command[1])
    elif command[0] == "pop":
        if len(items) > cnt:
            print(items[cnt])
            cnt += 1
        else:
            print(-1)
    elif command[0] == "empty":
        if len(items) == cnt:
            items = []
            cnt = 0
            print(1)
        else:
            print(0)
    elif command[0] == "size":
        print(len(items)-cnt)
    elif command[0] == "front":
        if len(items) > cnt:
            print(items[cnt])
        else:
            print(-1)
    elif command[0] == "back":
        if len(items) > cnt:
            print(items[-1])
        else:
            print(-1)