#!/usr/bin/env python
import sys
x = raw_input()
x = x.split(' ')

limit = 65535    

digit = []
for n in x:
    if n == '~':
        if len(digit) != 1:
            print 'ERROR'
            sys.exit(0)
        else:
            r = ~ digit[0]
            try:
                digit.pop()
            except:
                pass
            digit.append(r)
    elif n in ['+', '-', '|', '&', 'X']:
        try:
            if n == '+':
                r = digit[0] + digit[1]
            elif n == '-':
                r = digit[0] - digit[1]
            elif n == '&':
                r = digit[0] & digit[1]
            elif n == '|':
                r = digit[0] | digit[1]
            elif n == 'X':
                r = digit[0] ^ digit[1]
            elif n == '~':
                r = ~ digit[0]
            else:
                print 'ERROR'
                sys.exit(0)
        except:
            print 'ERROR'
            sys.exit(0)
        
        try:
            digit.pop()
        except:
            pass
        try:
            digit.pop()
        except:
            pass

        digit.append(r)
            
    else:
        digit.append(int(n, 16))
    
if r > limit:
    r = 'FFFF'
elif r < 0:
    r = '0000'
else:
    r = ('0000' + hex(r)[2:])
    r = r[-4:len(r)]

print r.upper()
