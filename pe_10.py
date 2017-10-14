"""
PE Problem 10
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

def sum_primes(max):
    if max < 3:
        return 0
    elif max == 3:
        return 2
    else:
        sum = 2
        trial = 3
        while trial < max:
            if is_prime(trial):
                sum += trial
            trial += 2
        return sum

print(sum_primes(2000000))
