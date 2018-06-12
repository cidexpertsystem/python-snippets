# Correct variable names consist only of English letters,
# digits and underscores and they can't start with a digit.

# Check if the given string is a correct variable name.

import re

def variableName(name):
    if re.search('[0-9]', name[0]):
        return False
    elif re.search('\s+', name):
        return False
    elif re.search('^[A-Za-z0-9_]+$', name):
        return True
    else:
        return False
