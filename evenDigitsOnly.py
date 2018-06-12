# Check if all digits of the given integer are even.

def evenDigitsOnly(n):
    test = str(n)
    for i in range(len(test)):
        if int(test[i]) % 2 == 1:
            return False
    return True
