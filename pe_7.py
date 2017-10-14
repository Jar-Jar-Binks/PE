"""
PE Problem 7
jar-jar-binks
09.21.2017
"""
from math import sqrt, floor
def is_prime(n):
    limit = floor(sqrt(n)) + 1
    for i in range(2,limit):
        if n % i == 0:
            return False
    return n

def find_prime(n1):
    count = 1
    value = 3
    if n1 ==1:
        return 2
    else:
        while count < n1:
            if is_prime(value):
                count += 1
            value +=2
        return value - 2

print(find_prime(10001))
