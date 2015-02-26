#!/usr/bin/pypy

'''
https://open.kattis.com/problems/t9spelling

To run:

py.test t9.py
'''

t9 = {
    'abc': 2,
    'def': 3,
    'ghi': 4,
    'jkl': 5,
    'mno': 6,
    'pqrs': 7,
    'tuv': 8,
    'wxyz': 9,
    ' ': 0
}

def get_value(char):
    for key, value in t9.iteritems():
        if char in key:
            return (key.index(char) + 1, value)


def func(string):
    output = ''
    for char in string:
        value = get_value(char)
        output += ''.join([str(value[1]) for x in range(value[0])])

    return output

def test_answer():
    assert func('hi') == '44444'
    assert func('yes') == '999337777'
    assert func('foo  bar') == '33366666600222777'
    assert func('hello world') == '4433555555666096667775553'