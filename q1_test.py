import math

def digit_length(n):
    return int(math.log10(n)) + 1 if n else 0

def square_digits(num):
	x = 0 ; y = 0; result = 0;
	for i in str(num):
		x = (int(i)**2); y = digit_length(result); result += x*(10**y) 
	return result

def test_q1():
    assert square_digits(9119) == 811181
    #assert square_digits(9) == 81