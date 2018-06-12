# In the popular Minesweeper game you have a board with some mines and
# those cells that don't contain a mine have a number in it that indicates
# the total number of mines in the neighboring cells.
# Starting off with some arrangement of mines we want to create
# a Minesweeper game setup.

def minesweeper(matrix):
    results = []
    if matrix == []:
        return []
    for i in range(len(matrix)):
        newList = []
        for j in range(len(matrix[0])):

            # count surrounding cells to get # of mines
            sum = 0
            if j < len(matrix[0])-1:
                sum += matrix[i][j+1]
            if j > 0:
                sum += matrix[i][j-1]
            if i < len(matrix)-1:
                sum += matrix[i+1][j]
            if i > 0:
                sum += matrix[i-1][j]
            if i < len(matrix)-1 and j < len(matrix[0])-1:
                sum += matrix[i+1][j+1]
            if i > 0 and j < len(matrix[i])-1:
                sum += matrix[i-1][j+1]
            if i < len(matrix)-1 and j > 0:
                sum += matrix[i+1][j-1]
            if i > 0 and j > 0:
                sum += matrix[i-1][j-1]
            newList.append(sum)
        results.append(newList)
    return results
