"""
PE Problem #001
Title: Multiples of 3 and 5
Written by Kris Bucyk (github.com/RiceKrisBs)
"""

def sum_multiples(x, y, z):
    # find the sum of all multiples of x or y below z
    if z < min(x, y):
        return 0

    total = 0
    for i in range(min(x, y), z):
        if i % x == 0 or i % y == 0:
            total += i
    return total


if __name__ == '__main__':
    print(sum_multiples(3, 5, 1000))
