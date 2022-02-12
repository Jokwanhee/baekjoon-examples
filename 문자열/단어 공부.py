'''
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
'''

n = input("")
n = n.upper()
list_n = sorted(list(set(n)))

dict_n = dict()
for i in range(len(list_n)):
    dict_n[list_n[i]] = n.count(list_n[i])

max_dict_n = max(dict_n.values())
count = 0
result = ""
for k, v in dict_n.items():
    if max_dict_n == v:
        count += 1
        result = k

if count >= 2:
    print("?")
else:
    print(result)
