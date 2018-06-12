# Given a string, replace each its character by the next one
# in the English alphabet (z would be replaced by a).

def alphabeticShift(inputString):
    answer = ""
    for C in inputString:
        if (C == 'z'):
            answer = answer + "a"
        else:
            answer = answer + chr(ord(C)+1)
    return answer
