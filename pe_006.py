"""
PE Problem #006
Title: Sum square difference
Written by Kris Bucyk (github.com/RiceKrisBs)
"""

def sum_square(n):
    return sum([n**2 for n in range(1, n + 1)])

def square_sum(n):
    return sum([n for n in range(1, n + 1)]) ** 2


if __name__ == '__main__':
    print(abs(sum_square(100) - square_sum(100)))
