def get_sum_of_divisors( number ):
    divisors = []
    possible_divisors = range( 1, number )
    
    for possible_divisor in possible_divisors:
        if( number % possible_divisor == 0 ):
            divisors.append( possible_divisor )
    
    return sum( divisors )

def f5(seq, idfun=None): # from http://www.peterbe.com/plog/uniqifiers-benchmark
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

amicable_numbers = []
numbers = range( 0, 10000 )

for number in numbers:
    sum_of_divisor = get_sum_of_divisors( number )
    
    if( number != sum_of_divisor ):
        if( get_sum_of_divisors( sum_of_divisor ) == number ):
            amicable_numbers.append( number )
            amicable_numbers.append( sum_of_divisor )

print sum( f5( amicable_numbers ) )