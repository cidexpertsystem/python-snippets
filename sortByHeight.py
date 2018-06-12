# Some people are standing in a row in a park. There are trees between
# them which cannot be moved. Your task is to rearrange the people by
# their heights in a non-descending order without moving the trees.

def sortByHeight(a):
    # rearrange elements other than -1 without moving the -1 positions
    x = sorted(a)
    b = [x for x in a if x != -1]
    c = sorted(b, reverse = True)

    for i in range(0, len(a)):
        if a[i] != -1:
            a[i] = c.pop()

    return a
