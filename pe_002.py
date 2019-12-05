"""
PE Problem #002
Title: Even Fibonacci numbers
Written by Kris Bucyk (github.com/RiceKrisBs)
"""

def find_fibonacci_sum(limit, option=0):
    # find sum of terms in Fibonacci sequence whose values do not exceed limit
    # option = 0: find sum of all Fibonacci terms <= limit
    # option = 1: find sum of all even Fibonacci terms <= limit
    # option = 2: find sum of all odd Fibonacci terms <= limit
    numbers = [1, 2]
    test_value = numbers[-1] + numbers[-2]
    while test_value <= limit:
        numbers.append(test_value)
        test_value = numbers[-1] + numbers[-2]

    if option in [1, 2]:
        return sum([x for x in numbers if x % 2 == (option - 1)])
    return sum(numbers)


if __name__ == '__main__':
    print(find_fibonacci_sum(4 * (10**6), option=1))
