"""
PE Problem 5
jar-jar-binks
09.14.2017
"""

# def multiple():
#     counter = 20
#     while True:
#         a = counter % 11
#         b = counter % 12
#         c = counter % 13
#         d = counter % 14
#         e = counter % 15
#         f = counter % 16
#         g = counter % 17
#         h = counter % 18
#         i = counter % 19
#         j = counter % 20
#         sum = a+b+c+d+e+f+g+h+i+j
#         #print(counter)
#         if sum == 0:
#             return counter
#         counter += 1

#print(multiple())
#print(1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20)
# 2  = 2^1
# 3  =     3^1
# 4  = 2^2
# 5  =         5^1
# 6  = 2^1 3^1
# 7  =             7^1
# 8  = 2^3
# 9  =     3^2
# 10 = 2^1     5^1
# 11 =                 11^1
# 12 = 2^2 3^1
# 13 =                      13^1
# 14 = 2^1         7^1
# 15 =     3^1 5^1
# 16 = 2^4
# 17 =                           17^1
# 18 = 2^1 3^2
# 19 =                                19^1
# 20 = 2^2     5^1

test = (2**4) * (3**2) * 5 * 7 * 11 * 13 * 17 * 19
a = test % 11
b = test % 12
c = test % 13
d = test % 14
e = test % 15
f = test % 16
g = test % 17
h = test % 18
i = test % 19
j = test % 20
sum = a+b+c+d+e+f+g+h+i+j
print(test)
