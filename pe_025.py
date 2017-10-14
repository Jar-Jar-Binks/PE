"""
PE Problem 25
jar-jar-binks
09.14.2017
"""

def fib(value):
    index = 2
    f_1 = 1
    f_2 = 2
    temp = 0
    while f_2 < value:
        temp = f_1 + f_2
        f_1 = f_2
        f_2 = temp
        index += 1
    return index + 1

print(fib(10 ** 999))
