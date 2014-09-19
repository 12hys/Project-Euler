#!/usr/bin/python

def special_cases( number ):
    hashmap = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
    }

    if number in hashmap.keys(): return hashmap[number]
    return None

def ones( number ):
    hashmap = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
    }

    if number in hashmap.keys(): return hashmap[number]
    return None

def tens( number ):
    if 20 <= number < 30: return 'twenty'
    if 30 <= number < 40: return 'thirty'
    if 40 <= number < 50: return 'forty'
    if 50 <= number < 60: return 'fifty'
    if 60 <= number < 70: return 'sixty'
    if 70 <= number < 80: return 'seventy'
    if 80 <= number < 90: return 'eighty'
    if 90 <= number < 100: return 'ninety'
    return None

def more( number ):
    if 100 <= number < 1000: return 'hundred'
    if 1000 <= number < 1000000: return 'million'
    return None

string = ''
for i in range( 1, 999 + 1 ):
    length_of_number = len( str( i ) )
    if( length_of_number == 1 ):
        string += ones( i )
    elif( length_of_number == 2 ):
        test_tens = special_cases( i )
        if( test_tens != None ):
            string += test_tens
        else:
            if( i % 10 == 0 ):
                string += tens( i )
            else:
                string += tens( i ) + str( ones( i % 10 ) )
    elif( length_of_number == 3 ):
        first_digit = int( str( i )[0] )
        string += ones( first_digit ) + str( more( i ) )

        base     = first_digit * 100
        tens_num = i - base

        if( tens_num >= 1 and tens_num < 10 ):
            string += 'and' + str( ones( tens_num ) )
        elif( tens_num >= 10 and tens_num < 20 ):
            string += 'and' + str( special_cases( tens_num ) )
        elif( tens_num >= 20 ):
            string += 'and'
            if( tens_num % 10 == 0 ):
                string += tens( tens_num )
            else:
                string += tens( tens_num ) + str( ones( tens_num % 10 ) )

print len( string + 'onethousand' )