#!/usr/bin/env python
import math, sys

def draw_sign(sign,char,size,spacing,n):
    string = ''
    for i in range(0,spacing):
        string = string + ' '    

    if(n == int(math.ceil(size/2))):
        if(sign == '-'):    
            for i in range(0,size):
                string = string + char
    else:
        for i in range(0,size):
            string = string + ' '
    return string


def draw_num(num,char,size,spacing,n):
    string = ''
    
    for i in range(0,spacing):
        string = string + ' '

    # 1111111111111111111111111111111
    if(num == 1):
        if(n == 0):
            for i in range(0,int(math.ceil(size/2))):
                string = string + ' '
            string = string + char
            for i in range(0,int(math.ceil(size/2))):
                string = string + ' '

        elif(n < size / 2):
            for i in range(0,int(math.ceil(size/2))-n):
                string = string + ' '
            string = string + char
            for i in range(0,n-1):
                string = string + ' '
            string = string + char
            for i in range(0,int(math.ceil(size/2))):
                string = string + ' '
        
        elif(n == size-1):
            for i in range(0,size):
                string = string + char
        else:
            for n in range(0,int(math.ceil(size/2))):
                string = string + ' '
            string = string + char
            for n in range(0,int(math.ceil(size/2))):
                string = string + ' '
    # 2222222222222222222222222222222
    elif(num == 2):
        if((n == 0) or (n == int(math.ceil(size/2))) or (n == size-1)):
            for i in range(0,size):
                string = string + char
        elif(n < size/2):
            for i in range(0,size-1):
                string = string + ' '
            string = string + char
        else:
            string = string + char
            for i in range(0,size-1):
                string = string + ' '
    # 33333333333333333333333333333333
    elif(num == 3):
        if((n == 0) or (n == int(math.ceil(size/2))) or (n == size-1)):
            for i in range(0,size):
                string = string + char
        else:
            for i in range(0,size-1):
                string = string + ' '
            string = string + char

    # 44444444444444444444444444444444
    elif(num == 4):
        if(n < size/2):
            string = string + char
            for n in range(0,size-2):
                string = string + ' '
            string = string + char
        elif(n == int(math.ceil(size/2))):
            for n in range(0,size):
                string = string + char
        else:
            for n in range(0,size-1):
                string = string + ' '
            string = string + char
    # 55555555555555555555555555555555
    elif(num == 5):
        if((n == 0) or (n == int(math.ceil(size/2))) or (n == size-1)):
            for i in range(0,size):
                string = string + char
        elif(n > size/2):
            for i in range(0,size-1):
                string = string + ' '
            string = string + char
        else:
            string = string + char
            for i in range(0,size-1):
                string = string + ' '
        
    # 66666666666666666666666666666666
    elif(num == 6):
        if((n == 0) or (n == int(math.ceil(size/2))) or (n == size-1)):
            for i in range(0,size):
                string = string + char
        elif(n > size/2):
            string = string + char
            for i in range(0,size-2):
                string = string + ' '
            string = string + char
        else:
            string = string + char
            for i in range(0,size-1):
                string = string + ' '
    # 77777777777777777777777777777777
    elif(num == 7):
        if(n == 0):
            for i in range(0,size):
                string = string + char
        else:
            for i in range(0,size-n-1):
                string = string + ' '
            string = string + char
            for i in range(0,n):
                string = string + ' '
        
    # 88888888888888888888888888888888
    elif(num == 8):
        if((n == 0) or (n == int(math.ceil(size/2))) or (n == size-1)):
            for i in range(0,size):
                string = string + char
        else:
            string = string + char
            for i in range(0,size-2):
                string = string + ' '
            string = string + char
    # 99999999999999999999999999999999
    elif(num == 9):
        if((n == 0) or (n == int(math.ceil(size/2))) or (n == size-1)):
            for i in range(0,size):
                string = string + char
        elif(n < size/2):        
            string = string + char
            for i in range(0,size-2):
                string = string + ' '
            string = string + char
        else:
            for i in range(0,size-1):
                string = string + ' '
            string = string + char
    # 00000000000000000000000000000000
    elif(num == 0):
        if((n == 0) or (n == size-1)):
            for i in range(0,size):
                string = string + char
        else:        
            string = string + char
            for i in range(0,size-2):
                string = string + ' '
            string = string + char
    else:
        pass

    return string

def draw_op(size,op,n):
    string = ''
    if(op == '+'):
        if((n == 0) or (n == size - 1)):
            for i in range(0,size):
                string = string + ' '
        elif(n == int(math.ceil(size/2))):
            for i in range(0,size):
                string = string + '+'
        else:
            for n in range(0,int(math.ceil(size/2))):
                string = string + ' '
            string = string + '+'
            for n in range(0,int(math.ceil(size/2))):
                string = string + ' '
    elif(op == '-'):
        if(n == int(math.ceil(size/2))):
            for i in range(0,size):
                string = string + '-'
        else:
            for i in range(0,size):
                string = string + ' '
    elif(op == '*'):
        if((n == 0) or (n == size - 1)):
            for i in range(0,size):
                string = string + ' '
        else:
            string = string + ' '
            for i in range(0,size-2):
                string = string + '*'
            string = string + ' '
    elif(op == '/'):
        for i in range(0,size-n-1):
            string = string + ' '
        string = string + '/'
        for i in range(0,n):
            string = string + ' ' 
    elif(op == '%'):
        length = int(math.floor(size/4))
        if(n < length):
            for i in range(0,length):
                string = string + '%'
            for i in range(0,size-n-1-length):
                string = string + ' '
            string = string + '%'
            for i in range(0,n):
                string = string + ' '
        elif(n > size-length-1):
            for i in range(0,size-n-1):
                string = string + ' '
            string = string + '%'
            for i in range(0,n-length):
                string = string + ' '
            for i in range(0,length):
                string = string + '%'
        else:
            for i in range(0,size-n-1):
                string = string + ' '
            string = string + '%'
            for i in range(0,n):
                string = string + ' ' 

    else:
        pass
    return string

def draw_space(size,spacing,n):
    string = ''
    for i in range(0,spacing):
        string = string + ' '
    for i in range(0,size):
        string = string + ' '
    return string

def draw_line(length,size,spacing,flag):
    string = ''
    line = ''
    for i in range(0,(size*length) + (spacing*(length-1))):
        string = string + ' '
    print string
    if(flag == 1):
        for i in range(0,(size*length) + (spacing*(length-1))):
            line = line + '-'
        print line
        print string

#......../ %%......%
#......./. %%.....%.
#....../.. ......%..
#...../... .....%...
#..../.... ....%....
#.../..... ...%.....
#../...... ..%......
#./....... .%.....%%
#/........ %......%%   

if __name__ == "__main__":
#    for n in range(0,size):
    int1 = raw_input()
    int2 = raw_input()
    operator = raw_input ()
    character = raw_input()
    size = raw_input()
    spacing = raw_input()
    #int1 = str(-555)
    #int2 = str(-666) 
    #size = 	5
    #operator = '+'
    #spacing = 2
    #character = '@'

    size = int(size)
    spacing = int(spacing)
    
    
    length = len(int1)+1
    if(length < len(str(int2))+1):
        length = len(int2)+1
    int1 = int(int1)
    int2 = int(int2)
    
    if(operator == '+'):
        result = int1 + int2
    elif(operator == '-'):
        result = int1 - int2
    elif(operator == '/'):
        result = int(int1 / int2)
    elif(operator == '*'):
        result = int1 * int2
    elif(operator == '%'):
        result = int1 % int2
    else:
        sys.exit(0)

    if(length < len(str(result))):
        length = len(str(result))

    int1 = ' ' + str(int1)
    int2 = str(int2)
    result = str(result)

    tmp = ''

    for n in range(0,length-len(int1)):
        tmp = tmp + ' '
    int1 = tmp + str(int1)
    
    tmp = operator
    for n in range(0,length-len(int2)-1):
        tmp = tmp + ' '
    int2 = tmp + int2
    tmp = ''

    for n in range(0,length-len(result)):
        tmp = tmp + ' '
    result = tmp + result


    string = ''
    # Line1

    for n in range(0,size):
        string = ''
        for m in range(0,length):
            if(int1[m] == ' '):
                if(m == 0):
                    string = string + draw_space(size,0,n) 
                else:
                    string = string + draw_space(size,spacing,n) 
            elif(int1[m] == '-'):
                string = string + draw_sign('-',character,size,spacing,n)
            else:
                string = string + draw_num(int(int1[m]),character,size,spacing,n)
        print string


    draw_line(length,size,spacing,0)
    for n in range(0,size):
        string = ''
        for m in range(0,length):
            if(int2[m] == ' '):
                if(m == 0):
                    string = string + draw_space(size,0,n) 
                else:
                    string = string + draw_space(size,spacing,n)  
            elif(int2[m] == '-'):
                string = string + draw_sign('-',character,size,spacing,n)
            elif((int2[m] == '-') or (int2[m] == '+') or (int2[m] == '/') or (int2[m] == '*') or (int2[m] == '%')):
                string = string + draw_op(size,int2[m],n)
            else:
                string = string + draw_num(int(int2[m]),character,size,spacing,n)
        print string

            
    draw_line(length,size,spacing,1)

    for n in range(0,size):
        string = ''
        for m in range(0,length):
            if(result[m] == ' '):
                if(result[m] == ' '):
                    if(m == 0):
                        string = string + draw_space(size,0,n) 
                    else:
                        string = string + draw_space(size,spacing,n) 
            elif(result[m] == '-'):
                string = string + draw_sign('-',character,size,spacing,n)
            elif((result[m] == '-') or (result[m] == '+') or (result[m] == '/') or (result[m] == '*') or (result[m] == '%')):
                string = string + draw_op(size,result[m],n)
            else:
                string = string + draw_num(int(result[m]),character,size,spacing,n)
        print string


