# Josephus problem
# https://www.geeksforgeeks.org/josephus-problem-set-2-simple-solution-k-2/
def josephus(n):
    # Find value of 2 ^ (1 + floor(Log n))
    # which is a power of 2 whose value
    # is just above n.
    p = 1
    while p <= n:
        p *= 2

    # Return 2n - 2^(1 + floor(Logn)) + 1
    return  2*n - p + 1

test = int(input())
result = []
for i in range(test):
    n = int(input())
    result.append(josephus(n))

for i in result:
    print(i)
