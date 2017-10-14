"""
PE Problem 4
jar-jar-binks
09.21.2017
"""

def is_palindrome(word):
    txt = str(word)
    backwards = txt[::-1]
    if txt == backwards:
        return True
    return False

def find_palindrome():
    n1 = 100
    largest_palindrome = 0
    while n1 <=999:
        n2 = n1
        while n2 <=999:
            prod = n1 * n2
            if is_palindrome(prod) and prod > largest_palindrome:
                largest_palindrome = prod
            n2 += 1
        n1 += 1
    return largest_palindrome

print(find_palindrome())
