#!/usr/bin/env python

if __name__ == "__main__":
    
    i = raw_input()
    i = i.split(',')
    p = 0
    
    if i[0] == i[1]:
        b = bin(int(i[0]))[2:]
        l = len(b)
        if l % 2 == 0:
            s1 = b[l/2:]
            s2 = b[:l/2]
        else: # odd
            s1 = b[l/2+1:]
            s2 = b[:l/2]
            
        if s1 == s2[::-1]:
            p = 1       
    else:
        
        for j in range(0,len(i)):
            i[j] = int(i[j])
            
            
        for j in range(i[0],i[1]):
            b = bin(j)[2:]
            
            l = len(b)
            if l % 2 == 0:
                s1 = b[l/2:]
                s2 = b[:l/2]
            else: # odd
                s1 = b[l/2+1:]
                s2 = b[:l/2]
                
            if s1 == s2[::-1]:
                p += 1
    print p       
            
