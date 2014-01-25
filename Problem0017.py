def special_cases( number ):
    if( number == 10 ):
        return 'ten'
    elif( number == 11 ):
        return 'eleven'
    elif( number == 12 ):
        return 'twelve'
    elif( number == 13 ):
        return 'thirteen'
    elif( number == 14 ):
        return 'fourteen'
    elif( number == 15 ):
        return 'fifteen'
    elif( number == 16 ):
        return 'sixteen'
    elif( number == 17 ):
        return 'seventeen'
    elif( number == 18 ):
        return 'eighteen'
    elif( number == 19 ):
        return 'nineteen'
    else:
        return None

def ones( number ):
    if( number == 0 ):
        return 'zero'
    elif( number == 1 ):
        return 'one'
    elif( number == 2 ):
        return 'two'
    elif( number == 3 ):
        return 'three'
    elif( number == 4 ):
        return 'four'
    elif( number == 5 ):
        return 'five'
    elif( number == 6 ):
        return 'six'
    elif( number == 7 ):
        return 'seven'
    elif( number == 8 ):
        return 'eight'
    elif( number == 9 ):
        return 'nine'
    else:
        return None

def tens( number ):
    if( number >= 20 and number < 30 ):
        return 'twenty'
    elif( number >= 30 and number < 40 ):
        return 'thirty'
    elif( number >= 40 and number < 50 ):
        return 'forty'
    elif( number >= 50 and number < 60 ):
        return 'fifty'
    elif( number >= 60 and number < 70 ):
        return 'sixty'
    elif( number >= 70 and number < 80 ):
        return 'seventy'
    elif( number >= 80 and number < 90 ):
        return 'eighty'
    elif( number >= 90 and number < 100 ):
        return 'ninety'
    else:
        return None

def more( number ):
    if( number >= 100 and number < 1000 ):
        return 'hundred'
    elif( number >= 1000 and number < 1000000 ):
        return 'million'
    else:
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

print string + 'onethousand'
print len( string + 'onethousand' )