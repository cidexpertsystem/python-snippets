# Given two strings, find the number of common characters between them.

def commonCharacterCount(s1, s2):
    s1_counts = {}
    s2_counts = {}

    if s1 == [] or s2 == []:
        return 0

    for letters in s1:
        if letters in s1_counts:
            s1_counts[letters] += 1
        else:
            s1_counts[letters] = 1

    for letters in s2:
        if letters in s2_counts:
            s2_counts[letters] += 1
        else:
            s2_counts[letters] = 1

    total_sum = 0

    if len(s1) <= len(s2):
        # check s1's letters in s2
        for letter in sorted(s1_counts):
            if letter in s2_counts and s2_counts[letter] >= s1_counts[letter]:
                total_sum += s1_counts[letter]
            elif letter in s2_counts:
                total_sum += s2_counts[letter]
    else:
        # check s2's letters in s1
        for letter in sorted(s2_counts):
            if letter in s1_counts and s1_counts[letter] >= s2_counts[letter]:
                total_sum += s2_counts[letter]
            elif letter in s1_counts:
                total_sum += s1_counts[letter]

    return total_sum
