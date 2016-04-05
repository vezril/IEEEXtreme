#!/usr/bin/python2.6

coord = raw_input()

(x1,y1,x2,y2) = coord.split(" ")
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

total = 0


while(True):
    x0 = x2 - x1
    y0 = y2 - y1
    if(x0 == 0):
        total = total + 2*y0
        break
    elif(y0 == 0):
        if(y0 == 1):
            total = total + 2
            break
        else:
            total = total + 2*x0 - 1
            break

    if(x0 > 0):
        x1 = x1 + 1
    else:
        x1 = x1 - 1
    print "(" + str(y1) + "," + str(x1) + ")"
    if(y0 > 0):
        y1 = y1 + 1
    else:
        y1 = y1 - 1

    total = total + 2
    print "(" + str(y1) + "," + str(x1) + ")"


print total*10
        
