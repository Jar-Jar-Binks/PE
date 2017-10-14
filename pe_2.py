"""
PE Problem 2
jar-jar-binks
08.30.2017
"""

from math import sqrt

def find_sum():
    partial = 0
    for i in range (1, 34):
        test_num = round((((1 + sqrt(5)) ** i) - ((1 - sqrt(5)) ** i)) / ((2 ** i) * sqrt(5)))
        if test_num % 2 == 0:
            partial = partial + test_num
        else:
            partial = partial
    print(partial)

find_sum()
