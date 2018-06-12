# Given two cells on the standard chess board,
# determine whether they have the same color or not.

import re

def chessBoardCellColor(cell1, cell2):
    return getColor(cell1) == getColor(cell2)




def getColor(cell):
    if int(cell[1]) % 2 == 0:
        # even row
        if re.search('[ACEG]', cell):
            return "dark"
        else:
            return "light"
    else:
        # odd row
        if re.search('[ACEG]', cell):
            return "light"
        else:
            return "dark"
