#!/usr/bin/env python2.6
import fileinput,sys,os

if __name__ == "__main__":
    
    VATS = []

#    while(True):
#        string = str(raw_input())
#        if not string: break
#        (number,money) = string.split(' ')
#        VATS.append((number,money))
    while(True):
        try:
            string = raw_input()
            if not string: break
            string = str(string)
            (number,money) = string.split(' ')
            VATS.append((number,money))
        except EOFError:
            break      
    #print VATS
    #sys.exit(1)

    total = 0
    
    for vat in VATS:
        number = ''
        n = 9 - len(vat[0])
        if(n > 1):
            continue
        for i in range(0,n):
            number = number + '0'
        number = number + vat[0]

        money = vat[1]



        S = (int(number[7]) * 2) + (int(number[6]) * 4) + (int(number[5]) * 8) + (int(number[4]) * 16) + (int(number[3]) * 32) + (int(number[2]) * 64) + (int(number[1]) * 128) + (int(number[0]) * 256)

        Y = S % 11
        if(((Y == 10) and (int(number[8])) == 0) or (Y == (int(number[8])))):
            total = total + int(money)
        
    print total
            


