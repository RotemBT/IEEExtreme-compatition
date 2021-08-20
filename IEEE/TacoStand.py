import statistics
import math

n = input()
result = []
for index in range(int(n)):
    s, m, r, b = map(int, input().split())
    x = min(m, r, b)
    y = statistics.median([m, r, b])
    z = max(m, r, b)
    if z > x + y:
        result.append(int(min(s, x + y)))
    else:
        result.append(int(min(s, math.floor((x + y + z) / 2))))

for i in result:
    print(i)
