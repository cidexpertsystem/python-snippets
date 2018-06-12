# Given an array of integers, find the maximal absolute difference
# between any two of its adjacent elements.

def arrayMaximalAdjacentDifference(inputArray):
    maxDiff = abs(inputArray[1] - inputArray[0])

    for i in range(1, len(inputArray)):
        diff = abs(inputArray[i] - inputArray[i-1])
        if diff > maxDiff:
            maxDiff = diff

    return maxDiff
