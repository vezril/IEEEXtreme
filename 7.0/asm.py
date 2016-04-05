#!/usr/bin/env python
'''

0104 89C3              MOV     BX,AX
0106 D1E8              SHR     AX,1

010C 91                XCHG    AX,CX
010D BA0102            MOV     DX,0201
0110 D1C2              ROL     DX,1

0112 D1EB              SHR     BX,1
0114 D1D1              RCL     CX,1
0116 38DE              CMP     DH,BL
0118 7EF6              JLE     0110
011A 38D3              CMP     BL,DL
011C 7E06              JLE     0124


0120 D1D1              RCL     CX,1


0124 28D4              SUB     AH,DL
0126 4A                DEC     DX
0127 20D0              AND     AL,DL
0129 21F2              AND     DX,SI
012B 38C2              CMP     DL,AL
012D 18E3              SBB     BL,AH
'''
global carry = 0         
global equal = 0
global less = 0
global greater = 0
global ax = 0
global bx = 0
global cx = 0
global dx = 0

def and8(x,y)
    x1 = ('00000000' + x)[-8:]
    y1 = ('00000000' + y)[-8:]
    return (x1 & y1)

def sbb(x):
    pass

def dec(x):
    return x-=1

def sub(x,y):
    bl = x-y

def jmp1():
    bx = ax
    ax = shr(ax)
    cx = ax
    dx = 201
    dx = rol(dx)
    bx = shr(bx)
    cx = rcl(cx)
    carry = 0
    cmp8()
    if less == 1 or equal == 1:
        jmp1()
    cmp8()
    if less == 1 or equal == 1:
        jmp2()
    cx = rcl(cx)
    jmp2()
    
def jmp2():
    sub()
    dx = dec(dx)
    #and
    #and
    cmp8()

def cmp8(x, y):
    if x == y:
        equal = 1
    if x <  y:
        less = 1
    
def ror(x):
    pass

def rol(x):
    return (x[-1] + x)[0:-1]

def shr(x):
    return x >> 1
    
def rcl(x):
    c = carry
    carry = x[0]
    return (x+c)[1:]


if __name__ == "__main__": 
    ax = int(raw_input())
    jmp1()




