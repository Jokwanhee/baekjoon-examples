'''
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
'''
import sys

C = int(input(""))

for i in range(C):
    result = 0
    sch_class = list(map(int, sys.stdin.readline().split()))
    try:
        if sch_class[0] == len(sch_class) - 1:
            students = sch_class[0]
            count = 0
            sch_class = sch_class[1:]
            for i in sch_class:
                result += i
            result = result / students
            for i in sch_class:
                if result < i:
                    count += 1
            result = count / students * 100
            print("{0:0.3f}%".format(result))
    except:
        break
