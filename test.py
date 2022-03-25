import sys
from collections import deque

d = deque(["1","2","3","4"])
e = deque([5,6,7,8])

d.reverse()

print(d)
a =""
a = "[" + ",".join(d)+ "]"
print(a)