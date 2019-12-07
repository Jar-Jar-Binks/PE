"""
PE Problem #003
Title: Largest prime factor
Written by Kris Bucyk (github.com/RiceKrisBs)
"""

import math

def is_prime(n):
    if n in [2, 3]:
        return True
    for i in range(2, math.ceil((n - 1) / 6)):
        if n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0:
            return False
    return True

def find_largest_prime_factor(number):
    limit = math.ceil(math.sqrt(number)) + 1
    largest_prime = number
    for k in range(2, math.ceil((limit - 1) / 6)):
        if number % (6 * k - 1) == 0 and is_prime(6 * k - 1):
            largest_prime = 6 * k - 1
        if number % (6 * k + 1) == 0 and is_prime(6 * k + 1):
            largest_prime = 6 * k + 1
    return largest_prime


if __name__ == '__main__':
    print(find_largest_prime_factor(600851475143))
