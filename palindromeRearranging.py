# Given a string, find out if its characters can be rearranged to form a palindrome.

def palindromeRearranging(inputString):
    letters = {}
    for letter in inputString:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    oddFound = False
    for x in sorted(letters):
        if letters[x] % 2 == 1:
            # odd number found
            if oddFound == True:
                return False
            else:
                oddFound = True
    return True
