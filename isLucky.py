# Ticket numbers usually consist of an even number of digits.
# A ticket number is considered lucky if the sum of the first half
# of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

import math

def isLucky(n):
    # if sum of first half of digits equals sum of last half, return true
    # calculate sum of first half of digits
    if len(str(n)) % 2 == 0:
        # even number of digits
        index = int(len(str(n)) / 2)
        firstHalf = str(n)[:index]
    else:
        # odd number of digits
        length = math.floor(len(str(n))/2)
        firstHalf = str(n)[:length]

    sum = 0
    for digits in firstHalf:
        sum += int(digits)

    # calculate sum of last half of digits
    if len(str(n)) % 2 == 0:
        # even number of digits
        length = math.floor(len(str(n))/2)
        lastHalf = str(n)[length:]
    else:
        # odd number of digits
        length = math.floor(len(str(n))/2)
        lastHalf = str(n)[length+1:]

    sum2 = 0
    for digits in lastHalf:
        sum2 += int(digits)

    if sum == sum2:
        return True
    else:
        return False
