N = int(input())
players = list(map(int, input().split()))
Q = int(input())
result=[]
for i in range(Q):
    G = int(input())
    # opposite G to find the number are available combine G
    oppositeG = ~G
    lowerThanG = []
    for player in players:
        if (oppositeG & player) == 0:
            lowerThanG.append(player)
    # check if the is sum of player are equal to G
    sum = 0
    for i in lowerThanG:
        sum |= i
    if sum != G:
        result.append('NO')
    else:
        result.append('YES')
for i in result:
    print(i)