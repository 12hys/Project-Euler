import calendar
from datetime import date

def run():
    twentieth_century = range( 1901, 2001 )
    months = range( 1, 13 )
    sunday_count = 0

    for year in twentieth_century:
        for month in months:
            if( date( year, month, 1 ).weekday() == 6 ):
                sunday_count += 1

    print( sunday_count )