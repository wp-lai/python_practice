"""
Author: Alan Lai
Date: Oct 19, 2016

Question:
Balanced parentheses means that each opening symbol 
has a corresponding closing symbol and the pairs of 
parentheses are properly nested. 
Write an algorithm that will read a string of parentheses 
from left to right and decide whether the symbols are balanced.

>>> is_balanced("(()()()())")
True
>>> is_balanced("(((())))")
True
>>> is_balanced("(()((())()))")
True
>>> is_balanced("((((((())")
False
>>> is_balanced("()))")
False
>>> is_balanced("(()()(()")
False
"""
def is_balanced(str_):
    stack = []
    for char in str_:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # empty stack
                return False
            if stack[-1] == '(': 
                stack.pop()
            else:
                return False
        else:  # pass other characters
            continue

    # return true if stack is still empty
    if stack:
        return False
    else:
        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()

