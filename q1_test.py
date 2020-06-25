def square_digits(num):
    pass

%나머지 //몫

import math

def digit_length(n):
    return int(math.log10(n)) + 1 if n else 0

def square_digits(num):
    a = num
    b = digit_length(a)
    e = 0
    count = 0
    while a < 10:
        c = a%10
        a = a // num
        d = c**2
        e += d
        count += digit_length(c)



def test_q1():
    assert square_digits(9119) == 811181