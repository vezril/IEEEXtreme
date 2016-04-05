#!/usr/bin/env python2.6

import copy

class Cube():  
    def __init__(self,colours):

        # Up-Left-Front-Right-Back-Down
        self.up = [[colours[0],colours[0],colours[0]],[colours[0],colours[0],colours[0]],[colours[0],colours[0],colours[0]]]
        self.left = [[colours[1],colours[1],colours[1]],[colours[1],colours[1],colours[1]],[colours[1],colours[1],colours[1]]]
        self.front = [[colours[2],colours[2],colours[2]],[colours[2],colours[2],colours[2]],[colours[2],colours[2],colours[2]]]
        self.right = [[colours[3],colours[3],colours[3]],[colours[3],colours[3],colours[3]],[colours[3],colours[3],colours[3]]]
        self.back = [[colours[4],colours[4],colours[4]],[colours[4],colours[4],colours[4]],[colours[4],colours[4],colours[4]]]
        self.bottom = [[colours[5],colours[5],colours[5]],[colours[5],colours[5],colours[5]],[colours[5],colours[5],colours[5]]]

        self.buffer1 = copy.deepcopy(self.left)
        self.buffer2 = self.front
###################################################################################        
    def rotate_left(self):
        self.buffer1 = copy.deepcopy(self.front)
        self.front[0][0] = self.up[0][2]
        self.front[0][1] = self.up[0][1]
        self.front[0][2] = self.up[0][0]

        self.buffer2 = copy.deepcopy(self.bottom)
        self.bottom[0][0] = self.buffer1[0][0]
        self.bottom[0][1] = self.buffer1[0][1]
        self.bottom[0][2] = self.buffer1[0][2]

        self.buffer1 = copy.deepcopy(self.back)
        self.back[0][0] = self.buffer2[0][2]
        self.back[0][1] = self.buffer2[0][1]
        self.back[0][2] = self.buffer2[0][0]

        self.up[0][0] = self.buffer1[0][0]
        self.up[0][1] = self.buffer1[0][1]
        self.up[0][2] = self.buffer1[0][2]

        self.buffer1 = copy.deepcopy(self.left)
        self.left[0][0] = self.buffer1[2][0]
        self.left[0][1] = self.buffer1[1][0]
        self.left[0][2] = self.buffer1[0][0]
        
        self.left[1][0] = self.buffer1[2][1]
        self.left[1][2] = self.buffer1[0][1]

        self.left[2][0] = self.buffer1[2][2]
        self.left[2][1] = self.buffer1[1][2]
        self.left[2][2] = self.buffer1[0][2]

###################################################################################    
    def rotate_right(self):
        self.buffer1 = copy.deepcopy(self.front)
        self.front[2][0] = self.up[2][2]
        self.front[2][1] = self.up[2][1]
        self.front[2][2] = self.up[2][0]

        self.buffer2 = copy.deepcopy(self.bottom)
        self.bottom[2][0] = self.buffer1[2][0]
        self.bottom[2][1] = self.buffer1[2][1]
        self.bottom[2][2] = self.buffer1[2][2]

        self.buffer1 = copy.deepcopy(self.back)
        self.back[2][0] = self.buffer2[2][2]
        self.back[2][1] = self.buffer2[2][1]
        self.back[2][2] = self.buffer2[2][0]

        self.up[2][0] = self.buffer1[2][0]
        self.up[2][1] = self.buffer1[2][1]
        self.up[2][2] = self.buffer1[2][2]

        self.buffer1 = copy.deepcopy(self.right)
        self.right[0][0] = self.buffer1[2][0]
        self.right[0][1] = self.buffer1[1][0]
        self.right[0][2] = self.buffer1[0][0]
        
        self.right[1][0] = self.buffer1[2][1]
        self.right[1][2] = self.buffer1[0][1]

        self.right[2][0] = self.buffer1[2][2]
        self.right[2][1] = self.buffer1[1][2]
        self.right[2][2] = self.buffer1[0][2]

###################################################################################  
    def rotate_vertical(self):
        self.buffer1 = copy.deepcopy(self.front)
        self.front[0][1] = self.up[2][1]
        self.front[1][1] = self.up[1][1]
        self.front[2][1] = self.up[0][1]

        self.buffer2 = copy.deepcopy(self.bottom)
        self.bottom[0][1] = self.buffer1[0][1]
        self.bottom[1][1] = self.buffer1[1][1]
        self.bottom[2][1] = self.buffer1[2][1]

        self.buffer1 = copy.deepcopy(self.back)
        self.back[0][1] = self.buffer2[2][1]
        self.back[1][1] = self.buffer2[1][1]
        self.back[2][1] = self.buffer2[0][1]

        self.up[0][1] = self.buffer1[0][1]
        self.up[1][1] = self.buffer1[1][1]
        self.up[2][1] = self.buffer1[2][1]



###################################################################################
    def rotate_up(self):
        self.buffer1 = copy.deepcopy(self.left)
        self.left[0][0] = self.front[2][0]
        self.left[0][1] = self.front[1][0]
        self.left[0][2] = self.front[0][0]

        self.buffer2 = copy.deepcopy(self.back)
        self.back[0][0] = self.buffer1[0][0]
        self.back[0][1] = self.buffer1[0][1]
        self.back[0][2] = self.buffer1[0][2]

        self.buffer1 = copy.deepcopy(self.right)
        self.right[0][0] = self.buffer2[0][2]
        self.right[0][1] = self.buffer2[0][1]
        self.right[0][2] = self.buffer2[0][0]

        self.front[0][0] = self.buffer1[0][0]
        self.front[0][1] = self.buffer1[0][1]
        self.front[0][2] = self.buffer1[0][2]

        self.buffer1 = copy.deepcopy(self.up)
        self.up[0][0] = self.buffer1[2][0]
        self.up[0][1] = self.buffer1[1][0]
        self.up[0][2] = self.buffer1[0][0]
        
        self.up[1][0] = self.buffer1[2][1]
        self.up[1][2] = self.buffer1[0][1]

        self.up[2][0] = self.buffer1[2][2]
        self.up[2][1] = self.buffer1[1][2]
        self.up[2][2] = self.buffer1[0][2]
       
###################################################################################
    def rotate_horizontal(self):
        self.buffer1 = copy.deepcopy(self.left)
        self.left[1][0] = self.front[1][2]
        self.left[1][1] = self.front[1][1]
        self.left[1][2] = self.front[1][0]

        self.buffer2 = copy.deepcopy(self.back)
        self.back[1][0] = self.buffer1[1][0]
        self.back[1][1] = self.buffer1[1][1]
        self.back[1][2] = self.buffer1[1][2]

        self.buffer1 = copy.deepcopy(self.right)
        self.right[1][0] = self.buffer2[1][2]
        self.right[1][1] = self.buffer2[1][1]
        self.right[1][2] = self.buffer2[1][0]

        self.front[1][0] = self.buffer1[1][0]
        self.front[1][1] = self.buffer1[1][1]
        self.front[1][2] = self.buffer1[1][2]

###################################################################################
    def rotate_bottom(self):
        self.buffer1 = copy.deepcopy(self.left)
        self.left[2][0] = self.front[2][2]
        self.left[2][1] = self.front[2][1]
        self.left[2][2] = self.front[2][0]

        self.buffer2 = copy.deepcopy(self.back)
        self.back[2][0] = self.buffer1[2][0]
        self.back[2][1] = self.buffer1[2][1]
        self.back[2][2] = self.buffer1[2][2]

        self.buffer1 = copy.deepcopy(self.right)
        self.right[2][0] = self.buffer2[2][2]
        self.right[2][1] = self.buffer2[2][1]
        self.right[2][2] = self.buffer2[2][0]

        self.front[2][0] = self.buffer1[2][0]
        self.front[2][1] = self.buffer1[2][1]
        self.front[2][2] = self.buffer1[2][2]

        self.buffer1 = copy.deepcopy(self.bottom)
        self.bottom[0][0] = self.buffer1[2][0]
        self.bottom[0][1] = self.buffer1[1][0]
        self.bottom[0][2] = self.buffer1[0][0]
        
        self.bottom[1][0] = self.buffer1[2][1]
        self.bottom[1][2] = self.buffer1[0][1]

        self.bottom[2][0] = self.buffer1[2][2]
        self.bottom[2][1] = self.buffer1[1][2]
        self.bottom[2][2] = self.buffer1[0][2]

###################################################################################
    def rotate_front(self):
        self.buffer1 = copy.deepcopy(self.right)
        self.right[0][0] = self.up[0][0]
        self.right[1][0] = self.up[1][0]
        self.right[2][0] = self.up[2][0]

        self.buffer2 = copy.deepcopy(self.bottom)
        self.bottom[0][0] = self.buffer1[2][0]
        self.bottom[1][0] = self.buffer1[1][0]
        self.bottom[2][0] = self.buffer1[0][0]

        self.buffer1 = copy.deepcopy(self.left)
        self.left[0][0] = self.buffer2[0][0]
        self.left[1][0] = self.buffer2[1][0]
        self.left[2][0] = self.buffer2[2][0]

        self.up[0][0] = self.buffer1[0][2]
        self.up[1][0] = self.buffer1[0][1]
        self.up[2][0] = self.buffer1[0][0]

        self.buffer1 = copy.deepcopy(self.front)
        self.front[0][0] = self.buffer1[2][0]
        self.front[0][1] = self.buffer1[1][0]
        self.front[0][2] = self.buffer1[0][0]

        self.front[1][0] = self.buffer1[2][1]
        self.front[1][2] = self.buffer1[0][1]

        self.front[2][0] = self.buffer1[2][2]
        self.front[2][1] = self.buffer1[1][2]
        self.front[2][2] = self.buffer1[0][2]

###################################################################################
    def rotate_back(self):
        self.buffer1 = copy.deepcopy(self.right)
        self.right[0][2] = self.up[0][2]
        self.right[1][2] = self.up[1][2]
        self.right[2][2] = self.up[2][2]

        self.buffer2 = copy.deepcopy(self.bottom)
        self.bottom[0][2] = self.buffer1[2][2]
        self.bottom[1][2] = self.buffer1[1][2]
        self.bottom[2][2] = self.buffer1[0][2]

        self.buffer1 = copy.deepcopy(self.left)
        self.left[0][2] = self.buffer2[0][2]
        self.left[1][2] = self.buffer2[1][2]
        self.left[2][2] = self.buffer2[2][2]

        self.up[0][2] = self.buffer1[2][2]
        self.up[1][2] = self.buffer1[1][2]
        self.up[2][2] = self.buffer1[0][2]

        self.buffer1 = copy.deepcopy(self.back)
        self.back[0][0] = self.buffer1[2][0]
        self.back[0][1] = self.buffer1[1][0]
        self.back[0][2] = self.buffer1[0][0]

        self.back[1][0] = self.buffer1[2][1]
        self.back[1][2] = self.buffer1[0][1]

        self.back[2][0] = self.buffer1[2][2]
        self.back[2][1] = self.buffer1[1][2]
        self.back[2][2] = self.buffer1[0][2]

    def rotate_middle(self):
        self.buffer1 = copy.deepcopy(self.right)
        self.right[1][0] = self.up[1][0]
        self.right[1][1] = self.up[1][1]
        self.right[1][2] = self.up[1][2]

        self.buffer2 = copy.deepcopy(self.bottom)
        self.bottom[1][0] = self.buffer1[2][1]
        self.bottom[1][1] = self.buffer1[1][1]
        self.bottom[1][2] = self.buffer1[0][1]

        self.buffer1 = copy.deepcopy(self.left)
        self.left[0][1] = self.buffer2[0][1]
        self.left[1][1] = self.buffer2[1][1]
        self.left[2][1] = self.buffer2[2][1]

        self.up[0][1] = self.buffer1[2][1]
        self.up[1][1] = self.buffer1[1][1]
        self.up[0][1] = self.buffer1[0][1]

        

    def print_front(self):
        print self.front[0][0] + " " + self.front[1][0] + " " + self.front[2][0]
        print self.front[0][1] + " " + self.front[1][1] + " " + self.front[2][1]
        print self.front[0][2] + " " + self.front[1][2] + " " + self.front[2][2]

    def print_back(self):
        print self.back[0][0] + " " + self.back[1][0] + " " + self.back[2][0]
        print self.back[0][1] + " " + self.back[1][1] + " " + self.back[2][1]
        print self.back[0][2] + " " + self.back[1][2] + " " + self.back[2][2] 

    def print_left(self):     
        print self.left[2][0] + " " + self.left[1][0] + " " + self.left[0][0]
        print self.left[2][1] + " " + self.left[1][1] + " " + self.left[0][1]
        print self.left[2][2] + " " + self.left[1][2] + " " + self.left[0][2] 

    def print_right(self):     
        print self.right[0][0] + " " + self.right[0][1] + " " + self.right[0][2]
        print self.right[1][0] + " " + self.right[1][1] + " " + self.right[1][2]
        print self.right[2][0] + " " + self.right[2][1] + " " + self.right[2][2]

    def print_up(self):     
        print self.up[0][2] + " " + self.up[1][2] + " " + self.up[2][2]
        print self.up[0][1] + " " + self.up[1][1] + " " + self.up[2][1]
        print self.up[0][0] + " " + self.up[1][0] + " " + self.up[2][0]

    def print_bottom(self):  
        print self.bottom[0][0] + " " + self.bottom[1][0] + " " + self.bottom[2][0]   
        print self.bottom[0][1] + " " + self.bottom[1][1] + " " + self.bottom[2][1]
        print self.bottom[0][2] + " " + self.bottom[1][2] + " " + self.bottom[2][2]



    def print_cube(self):
        print "Top"
        self.print_up()
        print "Front"
        self.print_front()
        print "Bottom"
        self.print_bottom()
        print "Back"
        self.print_back()
        print "Left"
        self.print_left()
        print "Right"
        self.print_right()





 
###################################################################################

#    F (Front): the side currently facing the solver
#    B (Back): the side opposite the front
#    f (Front two layers): the side facing the solver and the corresponding middle layer
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
        
if __name__ == "__main__":



    #colours = raw_input()
    colours = 'YRGOBW'
    #move = raw_input()	
    #move = "FL2R3'F"
    move = "RRRRR"
    r = Cube(colours)

#    try:
#        if(move[-1] == '\''):
#            tmp = int(move[-2])
#        else:
#            tmp = int(move[-1])
#        turns = tmp
#    except:
#        turns = 1
#        move = move + chr(turns)

#    for n in range(0,len(move)-1):
#        if(move[n] == '\''):
#            continue

#        if(move[n+1] == '\''):
#            reverse = 1
#        else:
#            reverse = 0

#        val = move[n]
#        x = turns

    x = len(move)
    n = 0
    while(n < x):
        val = move[n]
        try:
            turns = int(move[n+1])
            try:
                if(move[n+2] == '\''):
                    reverse = 1
                    n = n+2
            except:
                reverse = 0
                n = n + 1
        except:
            turns = 1
            try:
                if(move[n+1] == '\''):
                    reverse = 1
                    n = n+1
                else:
                    reverse = 0
            except:
               turns = 1

        n = n + 1
        while(turns != 0):
            #######################################
            if(val == 'u' or val == 'U'):
                if(reverse == 1):
                    r.rotate_up()
                else:
                    r.rotate_up()
                    r.rotate_up()
                    r.rotate_up()
                
                if(val == 'u'):
                    if(reverse == 1	):
                        r.rotate_horizontal()
                    else:
                        r.rotate_horizontal()
                        r.rotate_horizontal()
                        r.rotate_horizontal()

            #######################################
            elif(val == 'd' or val == 'D'):
                if(reverse == 1):
                    r.rotate_bottom()
                else:
                    r.rotate_bottom()
                    r.rotate_bottom()
                    r.rotate_bottom()
                
                if(val == 'd'):
                    if(reverse == 1):
                        r.rotate_horizontal()
                    else:
                        r.rotate_horizontal()
                        r.rotate_horizontal()
                        r.rotate_horizontal()
            #######################################
            elif(val == 'L' or val == 'l'):
                if(reverse == 0):
                    r.rotate_left()
                else:
                    r.rotate_left()
                    r.rotate_left()
                    r.rotate_left()

                if(val == 'l'):
                    if(reverse == 0):
                        r.rotate_vertical()
                    else:
                        r.rotate_vertical()
                        r.rotate_vertical()
                        r.rotate_vertical()

            #######################################
            elif(val == 'r' or val == 'R'):

                if(reverse == 1):
                    r.rotate_right()
                else:
                    r.rotate_right()
                    r.rotate_right()
                    r.rotate_right()

                if(val == 'r'):
                    if(reverse == 1):
                        r.rotate_vertical()
                    else:
                        r.rotate_vertical()
                        r.rotate_vertical()
                        r.rotate_vertical()
            #######################################
            elif(val == 'x' or val == 'X'):
                if(reverse == 1):
                    r.rotate_left()
                    r.rotate_vertical()
                    r.rotate_right()
                else:
                    r.rotate_left()
                    r.rotate_left()
                    r.rotate_left()
                    r.rotate_vertical()
                    r.rotate_vertical()
                    r.rotate_vertical()
                    r.rotate_right()
                    r.rotate_right()
                    r.rotate_right()
            #######################################
            elif(val == 'y' or val == 'Y'):
                if(reverse == 0):
                    r.rotate_up()
                    r.rotate_horizontal()
                    r.rotate_bottom()
                else:
                    r.rotate_up()
                    r.rotate_up()
                    r.rotate_up()
                    r.rotate_horizontal()
                    r.rotate_horizontal()
                    r.rotate_horizontal()
                    r.rotate_bottom()
                    r.rotate_bottom()
                    r.rotate_bottom()
            #######################################      
            elif(val == 'f' or val == 'F'):
                if(reverse == 0):
                    r.rotate_front()
                else:
                    r.rotate_front()
                    r.rotate_front()
                    r.rotate_front()

                if(val == 'f'):
                    if(reverse == 0):
                        r.rotate_middle()
                    else:
                        r.rotate_middle()
                        r.rotate_middle()
                        r.rotate_middle()
            #######################################
            elif(val == 'b' or val =='B'):
                if(reverse == 1):
                    r.rotate_back()
                else:
                    r.rotate_back()
                    r.rotate_back()
                    r.rotate_back()

                if(val == 'b'):
                    if(reverse == 1):
                        r.rotate_middle()
                    else:
                        r.rotate_middle()
                        r.rotate_middle()
                        r.rotate_middle()
            #######################################
            elif(val == 'z' or val == 'Z'):
                if(reverse == 0):
                    r.rotate_front()
                    r.rotate_middle()
                    r.rotate_back()
                else:
                    r.rotate_front()
                    r.rotate_middle()
                    r.rotate_back()
                    r.rotate_front()
                    r.rotate_middle()
                    r.rotate_back()
                    r.rotate_front()
                    r.rotate_middle()
                    r.rotate_back()
                
            turns = turns -1
            r.print_cube()
            raw_input()
    #r.print_cube()	
    r.print_front()

