# You are given an array of integers representing coordinates of obstacles
# situated on a straight line.

# Assume that you are jumping from the point with coordinate 0 to the right.
# You are allowed only to make jumps of the same length represented by some integer.

# Find the minimal length of the jump enough to avoid all the obstacles.

def avoidObstacles(inputArray):
    hopLength = 2
    while hopLength < 40:
        safe = True
        for nums in inputArray:
            if nums % hopLength == 0:
                safe = False
        if safe == True:
            return hopLength
        else:
            hopLength += 1
    return hopLength
