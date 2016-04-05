#!/usr/bin/python2.6

faces = raw_input()
move = raw_input()	
#    F (Front): the side currently facing the solver
#    B (Back): the side opposite the front
#    ƒ (Front two layers): the side facing the solver and the corresponding middle layer
#    b (Back two layers): the side opposite the front and the corresponding middle layer

#    U (Up): the side above or on top of the front side
#    D (Down): the side opposite the top, underneath the Cube
#    L (Left): the side directly to the left of the front
#    R (Right): the side directly to the right of the front

#    u (Up two layers) : the top side and the corresponding middle layer
#    d (Down two layers) : the bottom layer and the corresponding middle layer
#    l (Left two layers) : the side to the left of the front and the corresponding middle layer
#    r (Right two layers) : the side to the right of the front and the corresponding middle layer

#    x (rotate): rotate the entire Cube on R
#    y (rotate): rotate the entire Cube on U
#    z (rotate): rotate the entire Cube on F


def populate(colour):
    face = [['c','c','c'],['c','c','c'],['c','c','c']]
    for n in range(0,2):
        for m in range(0,2):
            face[n][m] = colour
    return face

up = populate(faces[0])
left = populate(faces[1])
front = populate(faces[2])
right = populate(faces[3])
back = populate(faces[4])
down = populate(faces[5])

try:
    tmp = int(move[-1])
    turns = tmp
except:
    turns = 1
    move = move + chr(turns)

for n in range(0,len(move)-1)
    if(move[n] == '\''):
        continue
    if(move[n+1] == '\''):
        reverse = 1
    else:
        revese = 0

    val = move[n]

    x = turns
    while(x != 0):
        if(val == 'u' or val == 'U'):
            if(reverse == 0):
                front[0] = right[0]           
            else:
                front[0] = left[0]
            
            if(val == 'u'):
                if(reverse == 0):
                    front[1] = right[1]
                else:
                    front[1] = left[1]

        elif(val == 'd' or val == 'D'):
            if(reverse == 0):
                front[0] =  left[0]          
            else:
                front[0] = right[0]
            
            if(val == 'D'):
                if(reverse == 0):
                    front[1] = left[1]
                else:
                    front[1] = right[1]

        elif(val == 'L' or val == 'l'):
            if(reverse == 0):
                front[0][0] = up[0][0]
                front[1][0] = up[1][0]
                front[2][0] = up[2][0]
            else:
                front[0][0] = down[2][0]
                front[1][0] = down[1][0]
                front[2][0] = down[0][0]

            if(val == 'l'):
                if(reverse == 0):
                    front[0][1] = up[0][1]
                    front[1][1] = up[1][1]
                    front[2][1] = up[2][1]
                else:
                    front[0][1] = down[2][1]
                    front[1][1] = down[1][1]
                    front[2][1] = down[0][1]

        elif(val == 'r' or val == 'R'):
            if(reverse == 0):
                front[0][2] = down[2][2]
                front[1][2] = down[1][2]
                front[2][2] = down[0][2]
            else:
                front[0][2] = up[0][2]
                front[1][2] = up[1][2]
                front[2][2] = up[2][2]

            if(val == 'r'):
                if(reverse == 0):
                    front[0][1] = down[2][1]
                    front[1][1] = down[1][1]
                    front[2][1] = down[0][1]
                else:
                    front[0][1] = up[0][1]
                    front[1][1] = up[1][1]
                    front[2][1] = up[2][1]

        elif(val == 'X' or val == 'x'):
        elif(val == 'y' or val == 'Y'):
        elif(val == 'Z' or val == 'z' or val == 'f' or val == 'F' or val == 'b' or val == 'B'):
        x = x -1


