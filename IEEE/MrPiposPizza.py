# https://en.wikipedia.org/wiki/Polygon_triangulation
from math import factorial

result = []
while True:
    try:
        slices = int(input())
        if slices == 1:
            print(3)
        elif slices == 2:
            print(4)
        else:
            for n in range(3, 1000):
                if factorial(2 * (n - 2)) // (factorial(n - 1) * factorial(n - 2)) == slices:
                    print(n)
                    break
    except:
        break
for i in result:
    print(i)
