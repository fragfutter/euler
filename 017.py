#!/usr/bin/python

t = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


def translate(n):
    if n < 20:
        return t[n]
    if n < 100:
        if n % 10 == 0:
            return t[n]
        else:
            return t[n // 10 * 10] + '-' + t[n % 10]  # twenty-three
    if n % 100 == 0:
        return t[n // 100] + ' hundred'
    return t[n // 100] + ' hundred and ' + translate(n % 100)


def numberlen(n):
    s = translate(n)
    s = s.replace(' ', '')
    s = s.replace('-', '')
    return len(s)

result = len('one thousand') - 1
for i in range(1, 1000):
    result += numberlen(i)
print(result)
