import math

# Python3 program to find (a^b) % MOD
# where a and b may be very large
# and represented as strings.
MOD = 1000000007


# https://www.geeksforgeeks.org/modulo-power-for-large-numbers-represented-as-strings/
# Returns modulo exponentiation
# for two numbers represented as
# long long int. It is used by
# powerStrings(). Its complexity
# is log(n)
def powerLL(x, n):
    result = 1
    while (n):
        if (n & 1):
            result = result * x % MOD
        n = int(n / 2)
        x = x * x % MOD
    return result

def factor(a,b):
    result=1
    for i in range(a,b+1):
        result*=i
# Returns modulo exponentiation
# for two numbers represented as
# strings. It is used by powerStrings()
def powerStrings(sa, sb):
    # We convert strings to number
    a = 0
    b = 0

    # calculating a % MOD
    for i in range(len(sa)):
        a = (a * 10 + (ord(sa[i]) -
                       ord('0'))) % MOD

    # calculating b % (MOD - 1)
    for i in range(len(sb)):
        b = (b * 10 + (ord(sb[i]) -
                       ord('0'))) % (MOD - 1)

    # Now a and b are long long int.
    # We calculate a^b using modulo
    # exponentiation
    return powerLL(a, b)


def modPow(b, e, m):
    r = 1
    b %= m
    while e > 0:
        if e % 2 == 1:
            r = (r * b) % m
        e = math.floor(e / 2)
        b = (b ** 2) % m
    return r


# Driver code

# As numbers are very large
# that is it may contains upto
# 10^6 digits. So, we use string.

t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    # binom = math.factorial(b)/(math.factorial(c)*math.factorial(b-c))
    if a != 1:
        binom = math.comb(b, c)
        print(powerStrings(str(a), str(binom)))
    else:
        print(1)
