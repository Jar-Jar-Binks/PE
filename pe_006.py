"""
PE Problem 6
jar-jar-binks
09.12.2017
"""

index = 100

def sum_square():
    sum_square_sum = 0
    for i in range(1,index+1):
        sum_square_sum = sum_square_sum + i **2
    return sum_square_sum

def square_sum():
    sum = 0
    for i in range(1,index+1):
        sum = sum + i
    return sum ** 2

def difference():
    return sum_square() - square_sum()

print(difference())
