"""
PE Problem 20
jar-jar-binks
09.23.2017
"""
from math import factorial

def find_sum(number):
    fact_num = factorial(number)
    txt_num = str(fact_num)
    num_length = len(txt_num)
    sum = 0
    for i in range(num_length):
        sum += int(txt_num[i])
    return sum

print(find_sum(100))
