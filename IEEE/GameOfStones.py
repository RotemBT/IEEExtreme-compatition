result = []
tests = int(input())
for test in range(tests):
    split = 0
    for game in range(int(input())):
        piles = int(input())
        pile = list(map(int, input().split(' ')))
        for i in pile:
            split += i//2

    if split % 2 == 0:
        result.append('Bob')
    else:
        result.append('Alice')

for i in result:
    print(i)
