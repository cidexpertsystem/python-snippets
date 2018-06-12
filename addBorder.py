# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

def addBorder(picture):
        result = []
        topRow = ""
        colNum = len(picture[0])
        topRow += (colNum + 2) * "*"

        result.append(topRow)

        for i in picture:
                row = "*" + i + "*"
                result.append(row)

        result.append(topRow)
        return result
