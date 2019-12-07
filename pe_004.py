"""
PE Problem #004
Title: Largest palindrome product
Written by Kris Bucyk (github.com/RiceKrisBs)
"""

def largest_palindrome(n):
    # finds largest palindrome made from the product of two n-digit numbers
    start = 10 ** (n - 1)
    largest_palindrome = 0

    # start testing pairs of n-digit numbers where n1 <= n2.
    for n1 in range(start, 10 ** n):
        n2 = n1
        while n2 < 10 ** n:
            temp_prod = n1 * n2
            if str(temp_prod) == str(temp_prod)[::-1] and temp_prod > largest_palindrome:
                largest_palindrome = temp_prod
            n2 += 1
    return largest_palindrome


if __name__ == '__main__':
    print(largest_palindrome(3))
