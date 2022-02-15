'''
세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.
정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.
============================================================================
모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
============================================================================
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

examples
============================================================================
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
============================================================================
'''


def checkP(p1, p2):
    if p1 == "(":
        if p2 == ")":
            return True
    elif p1 == "[":
        if p2 == "]":
            return True
    return False


def isValid(_items):
    n = input("")
    if n[0] == ".":
        return 0
    else:
        for i in n:
            if i == "(" or i == "[":
                _items.append(i)
            if i == ")" or i == "]":
                if len(_items) == 0:
                    return -1
                d = _items.pop()
                if checkP(d, i) == False:
                    return -1
        if len(_items):
            return -1
        return 1


while True:
    items = []
    _isValid = isValid(items)
    if _isValid == 0:
        break
    elif _isValid == 1:
        print("yes")
    else:
        print("no")
