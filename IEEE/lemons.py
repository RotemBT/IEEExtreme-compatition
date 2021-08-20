'''
algorithm- every time check if the middle have water, if true go to the lower mid otherwise go to the upper mid.
continue until find the broken one.
'''


def lemons(n, m, s):
    if n <= 2:
        return m + s
    middle = (n // 2) * m + s
    return middle + lemons(n - (n // 2), m, s)

n, m, s = map(int, input().split())
print(lemons(n, m, s))
