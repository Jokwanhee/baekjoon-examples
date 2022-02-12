# joonas 아이디 존재 시 --> joonas??!

id = input("")

if len(id) <= 50 and id.isalpha() and id.islower():
    print(id + "??!")