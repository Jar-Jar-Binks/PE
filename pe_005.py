"""
PE Problem #005
Title: Smallest multiple
Written by Kris Bucyk (github.com/RiceKrisBs)
"""

import pe_003

def find_product_of_primes(k):
    # finds product of all primes from 2 to k, inclusive
    prod = 1
    for i in range(2, k + 1):
        if pe_003.is_prime(i):
            prod *= i
    return prod

def find_smallest_multiple(k):
    # finds smallest positive number evenly divisible by 1 through k
    n1 = find_product_of_primes(k)
    n2 = 1
    divisors = [x for x in range(2, k + 1)]
    while True:
        test = n1 * n2
        if sum([test % i for i in divisors]) == 0:
            return test
        n2 += 1


if __name__ == '__main__':
    print(find_smallest_multiple(20))
