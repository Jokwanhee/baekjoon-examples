'''
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다.
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
이를 계산하는 프로그램을 작성하라.

=================examples=================
input : 8                                       input : 5
4   ++++- (1,2,3,4까지 삽입 후 4 삭제)             1   +- (1 삽입, 1 삭제)
3   - (1,2,3에서 3 삭제)                          2   +- (2 삽입, 2 삭제)
6   ++- (1,2,5,6 5와 6 삽입, 6 삭제)              5   +++- (3,4,5 삽입, 5 삭제)
8   ++- (1,2,5,7,8 7과 8 삽입, 8 삭제)            3   (3,4 중 3 삭제 ==> error)
7   - (1,2,5,7 중 7 삭제)                        4
5   - (1,2,5 중 5 삭제)                          *실패
2   - (1,2 중 2 삭제)
1   - (1 중 1 삭제)
*성공

=================시간 초과=================
int(input("")) => int(sys.stdin.readline())
items_op = [] => items_op = "" ( list -> string )
'''
import sys

T = int(input(""))

items = []
items_op = ""
max_num = 0
pop_item = 0

try:
    for i in range(T):
        n = int(sys.stdin.readline())
        if i == 0:
            for j in range(1, n + 1):
                items.append(j)
                items_op += "+"
            pop_item = items.pop()
            max_num = pop_item
            items_op += "-"
        else:
            if pop_item > n:
                if n in items:
                    pop_item = items.pop()
                    if pop_item == n:
                        items_op += "-"
                    else:
                        items_op += "!"
                else:
                    if pop_item - 1 == n:
                        pop_item = items.pop()
                        items_op += "-"
                    else:
                        items_op += "!"
            elif pop_item < n:
                for j in range(max_num + 1, n + 1):
                    items.append(j)
                    items_op += "+"
                pop_item = items.pop()
                max_num = pop_item
                items_op += "-"

    if "!" in items_op:
        print("NO")
    else:
        for i in items_op:
            print(i)
except:
    exit()





