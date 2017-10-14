"""
PE Problem 1
jar-jar-binks
08.30.2017
"""

def trial():
    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
        else:
            sum = sum
    print(sum)

trial()
