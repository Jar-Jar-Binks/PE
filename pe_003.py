"""
PE Problem #003
Title: Largest prime factor
Written by Kris Bucyk (github.com/RiceKrisBs)
"""

from math import sqrt, ceil

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return n

def find_largest_prime_factor(number):
    limit = ceil(sqrt(number)) + 1
    largest_prime = number
    for k in range (2,limit):
        if number % k == 0 and is_prime(k):
            largest_prime = is_prime(k)
    return largest_prime

print(find_largest_prime_factor(600851475143))
