import datetime
from math import *


def distance(lat1, long1, lat2, long2):
    return 2 * 6378.137 * asin(
        sqrt(sin((lat1 - lat2) / 2) ** 2 + cos(lat1) * cos(lat2) * abs(sin((long1 - long2) / 2) ** 2)))


lat1, long1 = map(float, input().split(','))
r = float(input())
result = dict()
title = list(map(str, input().split(',')))

while True:
    try:
        date, lan2, long2, phoneNumber = map(str, input().split(','))
        customersDistance = distance(radians(lat1), radians(long1), radians(float(lan2)), radians(float(long2)))
        date = datetime.datetime.strptime(date, "%m/%d/%Y %H:%M")
        if phoneNumber in result:
            if date > result[phoneNumber]:
                if r < customersDistance:
                    result.pop(phoneNumber)
                else:
                    result[phoneNumber] = date

        else:
            if r >= customersDistance:
                result[phoneNumber] = date
    except EOFError:
        break

print(','.join('{}'.format(k) for k in sorted(result)))
