# It seems like weighted interval scheduling problem for max profit of rental car
# https://www.techiedelight.com/weighted-interval-scheduling-problem/

# binary search on the given cars witch sorted by  finish time.
# return the last job which doesn't conflict with the given job.
def findLastNonConflictingJob(cars, n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if cars[mid][1] <= cars[n][0]:
            if cars[mid + 1][1] <= cars[n][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return None

# find the maximum profit of cars to rent with without overlapping time.
def findMaxProfit(cars):
    # construct a lookup table where the i'th index stores the maximum profit
    # for the first `i` jobs
    maxProfit = [None] * len(cars)
    maxProfit[0] = cars[0][2]
    # fill the `maxProfit` table in a bottom-up manner from the second index
    for i in range(1, len(cars)):
        # finding the next event that doesn't conflict
        index = findLastNonConflictingJob(cars, i)
        # include the current job with its non-conflicting jobs
        incl = cars[i][2]
        if index != None:
            incl += maxProfit[index]
        # store the maximum profit by including or excluding the current job
        maxProfit[i] = max(incl, maxProfit[i - 1])
    # return maximum profit
    return maxProfit[-1]


T = int(input())
for j in range(T):
    N = int(input())
    reservation = []
    for i in range(N):
        reservation.append(list(map(int, input().split(' '))))

    reservation.sort(reverse=False, key=lambda star: star[1])

    print(findMaxProfit(reservation))