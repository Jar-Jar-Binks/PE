"""
PE Problem 48
jar-jar-binks
09.12.2017
"""

def self_power(index):
    sum = 0
    for i in range(1,index+1):
        temp = (i ** i) % 10000000000
        sum += temp
    return sum % 10000000000

print(self_power(1000))
