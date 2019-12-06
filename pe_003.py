"""
PE Problem #003
Title: Largest prime factor
Written by Kris Bucyk (github.com/RiceKrisBs)
"""

import math


# TODO: refactor is_prime so that instead of checking all numbers up to n,
# it only checks up to math.ceil(math.sqrt(n))
# TODO: refactor is_prime so that instead of checking all numbers up to
# sqrt(n), it checks nubmers that are of the form 6i+-1 that are <= sqrt(n)
# TODO: refactor find_largest_prime_factor so that it only checks values that
# are of the form 6i+-1.
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_largest_prime_factor(number):
    limit = math.ceil(math.sqrt(number)) + 1
    largest_prime = number
    for k in range (2, limit):
        if number % k == 0 and is_prime(k):
            largest_prime = k
    return largest_prime


if __name__ == '__main__':
    print(find_largest_prime_factor(600851475143))
