# You have a string s that consists of English letters, punctuation marks,
# whitespace characters, and brackets. It is guaranteed that the parentheses
# in s form a regular bracket sequence.

# Your task is to reverse the strings contained in each pair of matching parentheses,
# starting from the innermost pair. The results string should not contain any parentheses.

def reverseParentheses(s):
        # reverse the strings contained in each pair of matching parentheses,
        # starting from the innermost pair. The results string should not contain any parentheses.
        parens = []
        buffer = ""
        for i in range(len(s)):
                if s[i] == ')':
                        right = i
                        left = parens.pop()
                        s = s[:left] + s[left:right][::-1] + s[right:]
                elif s[i] == '(':
                        parens.append(i)

        s = s.replace(')', '')
        s = s.replace('(', '')

        return s
