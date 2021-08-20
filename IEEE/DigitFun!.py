def digitFun(someString):
    a = int(someString)
    if a == len(someString):
        return 1
    return digitFun(str(len(someString))) + 1

result = []
s = str(input())
while s != 'END':
    result.append(digitFun(s))
    s = str(input())

for i in result:
    print(i)

