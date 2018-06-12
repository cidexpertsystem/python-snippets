# Two arrays are called similar if one can be obtained from another by
# swapping at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.

def areSimilar(a, b):
    # Two arrays are called similar if one can be obtained from
    # another by swapping at most one pair of elements in one of the arrays.

    # Given two arrays a and b, check whether they are similar.

    # First, the sorted arrays have to match or else they can't be similar
    if sorted(a) != sorted(b):
        return False
    elif a == b:
        return True
    else:
        # the number of differences has to be 2 to pass
        diffs = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diffs += 1
        if diffs == 2:
            return True
        else:
            return False
