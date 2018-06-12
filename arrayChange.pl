# You are given an array of integers. On each move you are allowed to
# increase exactly one of its element by one. Find the minimal number of
# moves required to obtain a strictly increasing sequence from the input.

import math

def arrayChange(inputArray):
    changeCount = 0
    if len(inputArray) < 2:
        return 0
    for i in range(1,len(inputArray)):
        if (inputArray[i] <= inputArray[i-1]):
            changeCount += abs(inputArray[i] - inputArray[i-1]) + 1
            inputArray[i] += abs(inputArray[i] - inputArray[i-1]) + 1
    return changeCount
