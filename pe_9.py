"""
PE Problem 9
jar-jar-binks
09.16.2017
"""

# a = k*(m**2-n**2)
# b = k*(2*m*n)
# c = k*(m**2+n**2)

def find_triplet():
    k = 1
    n = 1
    m = 2
    a = k * (m**2 - n**2)
    b = k * (2 * m * n)
    c = k * (m**2 + n**2)
    sum = a + b + c
    while sum <= 1000:
        a = k * (m**2 - n**2)
        b = k * (2 * m * n)
        c = k * (m**2 + n**2)
        sum = a + b + c
        if sum == 1000:
            return(a * b * c)
        while sum <=1000 and n < m:
            a = k * (m**2 - n**2)
            b = k * (2 * m * n)
            c = k * (m**2 + n**2)
            sum = a + b + c
            if sum == 1000:
                return(a * b * c)
            while sum <= 1000:
                a = k * (m**2 - n**2)
                b = k * (2 * m * n)
                c = k * (m**2 + n**2)
                sum = a + b + c
                if sum == 1000:
                    return(a * b * c)
                m += 1
            m = 2
            a = k * (m**2 - n**2)
            b = k * (2 * m * n)
            c = k * (m**2 + n**2)
            sum = a + b + c
            n += 1
        m = 2
        n = 1
        a = k * (m**2 - n**2)
        b = k * (2 * m * n)
        c = k * (m**2 + n**2)
        sum = a + b + c
        k += 1

print(find_triplet())
