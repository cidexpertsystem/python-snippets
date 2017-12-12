# Cindy Reichel
# 2017/12/08
def containsCloseNums(nums, k):
    results = {}

    # scan sorted array to see if every number is unique
    if (len(set(nums)) == len(nums)):
        return False

    # if there are duplicates, use dictionary to find them
    for i in range(0, len(nums)):
        results = {}
        counts = []
        for j in range(0,k+1):
            if (i + j < len(nums)):
                if (nums[i+j] in results):
                    results[nums[i+j]] += 1
                else:
                    results[nums[i+j]] = 1
        counts = sorted(results.values())
        if (counts != [] and counts[len(results) - 1] > 1):
            return True
    return False
