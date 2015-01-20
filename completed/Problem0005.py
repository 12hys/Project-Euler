#!/usr/bin/python

x = 1


def loop(start):
    passAll = 0
    for ctr in range(1, 21):
        if(start % ctr == 0):
            passAll += 1
        else:
            break
    if(passAll == 20):
        return True
    else:
        if(passAll > 15):
            print(
                str(start) + " passed the first " + str(passAll) + " numbers.")
        return False

while(loop(x) == False):
    x += 1

print("Number: " + str(x))
