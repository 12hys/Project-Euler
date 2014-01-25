'''
Created on Jul 24, 2011

@author: Rhys
'''

#correct values: func(4) = 15 and func(5) = 35
def run():
    def func(x):
        if(x==1): return 1
        return n+(n-1)
        #return func(x-1)+2**(x-1)

    print( func(5) )