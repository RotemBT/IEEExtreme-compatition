# It seems like weighted interval scheduling problem for max profit of rental car
# https://www.techiedelight.com/weighted-interval-scheduling-problem/
def findLastNonConflictingJob(stars, n):
    # binary search
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if stars[mid][1] <= stars[n][0]:
            if stars[mid + 1][1] < stars[n][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return None


def findMaxProfit(stars):
    # create an array where index x is the best option include the X event (by sort order)
    maxDesirability = [None] * len(stars)
    maxDesirability[0] = stars[0][2]
    for i in range(1, len(stars)):
        # finding the next event that doesn't conflict
        index = findLastNonConflictingJob(stars, i)
        incl = stars[i][2]
        # if you found an index add to the profits his value (the last none conflict event)
        if index != None:
            incl += maxDesirability[index]
        # the value of the current call will be the max between the last call and what we got
        maxDesirability[i] = max(incl, maxDesirability[i - 1])
    # return the last value
    return maxDesirability[-1]

N = int(input())
L = []
for i in range(N):
    L.append(list(map(int, input().split(' '))))

L.sort(reverse=False, key=lambda star: star[1])

print(findMaxProfit(L))
