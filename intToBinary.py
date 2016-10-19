"""
Author: Alan Lai
Date: Oct 19, 2016

Question:
Converting decimal numbers to binary numbers

>>> convert_to_binary(25)
'0b11001'

>>> convert_to_binary(233)
'0b11101001'
"""
# Solution 1: 
# keep dividing by 2, store the remainder in a stack
# read in reverse order
def convert_to_binary(number):
    stack = []
    while number:
        stack.append(number % 2)
        number = number // 2
    binary_str = "0b"
    while stack:
        binary_str += str(stack.pop())
    return binary_str


# Solution 2: using built-in function bin
def convert_to_binary(number):
    return bin(number)


if __name__ == '__main__':
    import doctest
    doctest.testmod()