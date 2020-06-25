def get_count(input_str):
    mo = ['a','e','i','o','u','A','E','I','O','U']
    while 1:
        if input_str == '#':
            return

        cnt = 0
        for i in range(len(input_str)):
            if input_str[i] in mo:
                cnt += 1

        return cnt

# tester provided
def test_sample():
    assert get_count("abracadabra") == 5
    assert get_count("") == 0
    assert get_count("bcd,! ?") == 0
    assert get_count("pear tree") == 4
    assert get_count("o a kak ushakov lil vo kashu kakao") == 13
