"""
PE Problem #003
Title: Largest prime factor
Written by Kris Bucyk (github.com/RiceKrisBs)
"""

import math

def is_prime(n):
    # first check if n is 2 or 3
    if n in [2, 3]:
        return True
    # next check if n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # prime numbers are of the form 6i+- 1
    # check if any numbers of this form divide n
    for i in range(2, math.ceil((n - 1) / 6)):
        if n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0:
            return False
    return True

# TODO: fixed an error in find_largest_prime_factor but it now runs
# too slowly. Update function to run in reasonable amount of time
def find_largest_prime_factor(number):
    limit = math.ceil((number - 1) / 6) + 1
    largest_prime = number
    for k in range(2, limit):
        if number % (6 * k - 1) == 0 and is_prime(6 * k - 1):
            largest_prime = 6 * k - 1
        if number % (6 * k + 1) == 0 and is_prime(6 * k + 1):
            largest_prime = 6 * k + 1
    return largest_prime


if __name__ == '__main__':
    print(find_largest_prime_factor(600851475143))
    # print(find_largest_prime_factor(34))
