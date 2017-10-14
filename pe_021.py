"""
PE Problem 21
jar-jar-binks
09.23.2017
"""
#NOTE TO SELF: I BROKE FUNCTION D(NUM_A) TRYING TO OPTOMIZE IT. FIX IT AT SOME POINT.
from math import sqrt, ceil
def d(num_a):
    sum = 0
    for i in range(1,ceil(sqrt(num_a)) +1):
        if num_a % i == 0:
            sum = sum + i + (num_a/i)
    return sum

def find_amicable(cap):
    n1 = 2
    sum = 0
    while n1 < cap + 2:
        n2 = d(n1)
        if d(n2) == n1 and n2 != n1:
            sum = sum + n1 + n2
        n1 += 1
    return sum/2

print(find_amicable(10000))
