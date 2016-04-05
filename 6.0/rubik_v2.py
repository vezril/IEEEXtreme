#!/usr/bin/env python2.6

import copy

class Cube():
    '''
        Left - left
        Face - front
        Right - Side 3
        Back - Side 4
        Top - Side 5
        Bottom - bottom
    '''
    
    def __init__(self):
        self.left = [['g','g','g'],['g','g','g'],['g','g','g']]
        self.front = [['p','p','p'],['p','p','p'],['p','p','p']]
        self.right = [['b','b','b'],['b','b','b'],['b','b','b']]
        self.back = [['x','x','x'],['x','x','x'],['x','x','x']]
        self.up = [['r','r','r'],['r','r','r'],['r','r','r']]
        self.bottom = [['o','o','o'],['o','o','o'],['o','o','o']]
        self.buffer1 = self.left
        self.buffer2 = self.front
###################################################################################        
    def rotate_left(self,direction):
        # Modification of side, 2,4,5 and 6
        if(direction == 'reverse'):
            self.buffer1 = copy.deepcopy(self.up)
            self.up[0][0] = self.front[0][0]
            self.up[1][0] = self.front[1][0]
            self.up[2][0] = self.front[2][0]
            
            self.buffer2 = copy.deepcopy(self.back)
            self.back[0][0] = self.buffer1[2][0]
            self.back[1][0] = self.buffer1[1][0]
            self.back[2][0] = self.buffer1[0][0]
            
            self.buffer1 = copy.deepcopy(self.bottom)
            self.bottom[2][0] = self.buffer2[0][0]
            self.bottom[1][0] = self.buffer2[1][0]
            self.bottom[0][0] = self.buffer2[2][0]
            
            self.front[0][0] = self.buffer1[0][0]
            self.front[1][0] = self.buffer1[1][0]
            self.front[2][0] = self.buffer1[2][0]
            
            # Rotation of side
            self.buffer1 = copy.deepcopy(self.left)
            self.left[0][0] = self.buffer1[2][0]
            self.left[0][1] = self.buffer1[1][0]
            self.left[0][2] = self.buffer1[0][0]
            
            self.left[1][0] = self.buffer1[2][1]
            self.left[1][2] = self.buffer1[0][1]
            
            self.left[2][0] = self.buffer1[2][2]
            self.left[2][1] = self.buffer1[1][2]
            self.left[2][2] = self.buffer1[0][2]
           

        elif(direction == 'normal'):
            self.buffer1 = copy.deepcopy(self.bottom)
            self.bottom[0][0] = self.front[0][0]
            self.bottom[1][0] = self.front[1][0]
            self.bottom[2][0] = self.front[2][0]
            
            self.buffer2 = copy.deepcopy(self.back)
            self.back[0][0] = self.buffer1[2][0]
            self.back[1][0] = self.buffer1[1][0]
            self.back[2][0] = self.buffer1[0][0]
            
            self.buffer1 = copy.deepcopy(self.up)
            self.up[2][0] = self.buffer2[0][0]
            self.up[1][0] = self.buffer2[1][0]
            self.up[0][0] = self.buffer2[2][0]
            
            self.front[0][0] = self.buffer1[0][0]
            self.front[1][0] = self.buffer1[1][0]
            self.front[2][0] = self.buffer1[2][0]
            
            # Rotation of side
            self.buffer1 = copy.deepcopy(self.left)
            self.left[0][0] = self.buffer1[0][2]
            self.left[0][1] = self.buffer1[1][2]
            self.left[0][2] = self.buffer1[2][2]
            
            self.left[1][0] = self.buffer1[0][1]
            self.left[1][2] = self.buffer1[2][1]
            
            self.left[2][0] = self.buffer1[0][0]
            self.left[2][1] = self.buffer1[1][0]
            self.left[2][2] = self.buffer1[2][0]
            
        else:
            print "Invalid direction in rotate_left() method"
###################################################################################    
    def rotate_bottom(self,direction):
        if(direction == 'normal'):
            self.buffer1 = copy.deepcopy(self.front)
            self.front[2][0] = self.left[2][0]
            self.front[2][1] = self.left[2][1]
            self.front[2][2] = self.left[2][2]
            
            self.buffer2 = copy.deepcopy(self.right)
            self.right[2][0] = self.buffer1[2][0]
            self.right[2][1] = self.buffer1[2][1]
            self.right[2][2] = self.buffer1[2][2]
            
            self.buffer1 = copy.deepcopy(self.back)
            self.back[2][0] = self.buffer2[2][2]
            self.back[2][1] = self.buffer2[2][1]
            self.back[2][2] = self.buffer2[2][0]
            
            self.left[2][0] = self.buffer1[2][2]
            self.left[2][1] = self.buffer1[2][1]
            self.left[2][2] = self.buffer1[2][0]
            
            self.buffer1 = copy.deepcopy(self.up)
            self.up[0][0] = self.buffer1[2][0]
            self.up[0][1] = self.buffer1[1][0]
            self.up[0][2] = self.buffer1[0][0]

            self.up[1][0] = self.buffer1[2][1]
            self.up[1][2] = self.buffer1[0][1]

            self.up[2][0] = self.buffer1[2][2]
            self.up[2][1] = self.buffer1[1][2]
            self.up[2][2] = self.buffer1[0][2]
            
        
        elif(direction == 'left'):
        
            self.buffer1 = copy.deepcopy(self.back)
            self.back[2][0] = self.left[2][2]
            self.back[2][1] = self.left[2][1]
            self.back[2][2] = self.left[2][0]
            
            self.buffer2 = copy.deepcopy(self.right)
            self.right[2][0] = self.buffer1[2][2]
            self.right[2][1] = self.buffer1[2][1]
            self.right[2][2] = self.buffer1[2][0]
            
            self.buffer1 = copy.deepcopy(self.front)
            self.front[2][0] = self.buffer2[2][2]
            self.front[2][1] = self.buffer2[2][1]
            self.front[2][2] = self.buffer2[2][0]
            
            self.left[2][0] = self.buffer1[2][0]
            self.left[2][1] = self.buffer1[2][1]
            self.left[2][2] = self.buffer1[2][2]
            
            self.buffer1 = copy.deepcopy(self.up)
            self.up[0][0] = self.buffer1[2][0]
            self.up[0][1] = self.buffer1[1][0]
            self.up[0][2] = self.buffer1[0][0]

            self.up[1][0] = self.buffer1[2][1]
            self.up[1][2] = self.buffer1[0][1]

            self.up[2][0] = self.buffer1[2][2]
            self.up[2][1] = self.buffer1[1][2]
            self.up[2][2] = self.buffer1[0][2]
        
        else:
            print "Invalid direction in rotate_top() method"
###################################################################################            
    def rotate_right(self,direction):
        # Modification of side, 2,4,5 and 6
        if(direction == 'up'):
            self.buffer1 = copy.deepcopy(self.up)
            self.up[0][0] = self.front[0][0]
            self.up[1][0] = self.front[1][0]
            self.up[2][0] = self.front[2][0]
            
            self.buffer2 = copy.deepcopy(self.back)
            self.back[0][0] = self.buffer1[2][0]
            self.back[1][0] = self.buffer1[1][0]
            self.back[2][0] = self.buffer1[0][0]
            
            self.buffer1 = copy.deepcopy(self.bottom)
            self.bottom[2][0] = self.buffer2[0][0]
            self.bottom[1][0] = self.buffer2[1][0]
            self.bottom[0][0] = self.buffer2[2][0]
            
            self.front[0][0] = self.buffer1[0][0]
            self.front[1][0] = self.buffer1[1][0]
            self.front[2][0] = self.buffer1[2][0]
            
            # Rotation of side
            self.buffer1 = copy.deepcopy(self.left)
            self.left[0][0] = self.buffer1[2][0]
            self.left[0][1] = self.buffer1[1][0]
            self.left[0][2] = self.buffer1[0][0]
            
            self.left[1][0] = self.buffer1[2][1]
            self.left[1][2] = self.buffer1[0][1]
            
            self.left[2][0] = self.buffer1[2][2]
            self.left[2][1] = self.buffer1[1][2]
            self.left[2][2] = self.buffer1[0][2]
           

        elif(direction == 'down'):
            self.buffer1 = copy.deepcopy(self.bottom)
            self.bottom[0][0] = self.front[0][0]
            self.bottom[1][0] = self.front[1][0]
            self.bottom[2][0] = self.front[2][0]
            
            self.buffer2 = copy.deepcopy(self.back)
            self.back[0][0] = self.buffer1[2][0]
            self.back[1][0] = self.buffer1[1][0]
            self.back[2][0] = self.buffer1[0][0]
            
            self.buffer1 = copy.deepcopy(self.up)
            self.up[2][0] = self.buffer2[0][0]
            self.up[1][0] = self.buffer2[1][0]
            self.up[0][0] = self.buffer2[2][0]
            
            self.front[0][0] = self.buffer1[0][0]
            self.front[1][0] = self.buffer1[1][0]
            self.front[2][0] = self.buffer1[2][0]
            
            # Rotation of side
            self.buffer1 = copy.deepcopy(self.left)
            self.left[0][0] = self.buffer1[0][2]
            self.left[0][1] = self.buffer1[1][2]
            self.left[0][2] = self.buffer1[2][2]
            
            self.left[1][0] = self.buffer1[0][1]
            self.left[1][2] = self.buffer1[2][1]
            
            self.left[2][0] = self.buffer1[0][0]
            self.left[2][1] = self.buffer1[1][0]
            self.left[2][2] = self.buffer1[2][0]
            
        else:
            print "Invalid direction in rotate_right() method"

###################################################################################
    def rotate_bottom(self,direction):
        if(direction == 'right'):
            self.buffer1 = copy.deepcopy(self.front)
            self.front[0][0] = self.left[0][0]
            self.front[0][1] = self.left[0][1]
            self.front[0][2] = self.left[0][2]
            
            self.buffer2 = copy.deepcopy(self.right)
            self.right[0][0] = self.buffer1[0][0]
            self.right[0][1] = self.buffer1[0][1]
            self.right[0][2] = self.buffer1[0][2]
            
            self.buffer1 = copy.deepcopy(self.back)
            self.back[0][0] = self.buffer2[0][2]
            self.back[0][1] = self.buffer2[0][1]
            self.back[0][2] = self.buffer2[0][0]
            
            self.left[0][0] = self.buffer1[0][2]
            self.left[0][1] = self.buffer1[0][1]
            self.left[0][2] = self.buffer1[0][0]
            
            self.buffer1 = copy.deepcopy(self.bottom)
            self.bottom[0][0] = self.buffer1[0][2]
            self.bottom[0][1] = self.buffer1[1][2]
            self.bottom[0][2] = self.buffer1[2][2]
                                            
            self.bottom[1][0] = self.buffer1[0][1]
            self.bottom[1][2] = self.buffer1[2][1]
                                            
            self.bottom[2][0] = self.buffer1[0][0]
            self.bottom[2][1] = self.buffer1[1][0]
            self.bottom[2][2] = self.buffer1[2][0]
            
    
        elif(direction == 'left'):
        
            self.buffer1 = copy.deepcopy(self.back)
            self.back[0][0] = self.left[0][2]
            self.back[0][1] = self.left[0][1]
            self.back[0][2] = self.left[0][0]
            
            self.buffer2 = copy.deepcopy(self.right)
            self.right[0][0] = self.buffer1[0][2]
            self.right[0][1] = self.buffer1[0][1]
            self.right[0][2] = self.buffer1[0][0]
            
            self.buffer1 = copy.deepcopy(self.front)
            self.front[0][0] = self.buffer2[0][2]
            self.front[0][1] = self.buffer2[0][1]
            self.front[0][2] = self.buffer2[0][0]
            
            self.left[0][0] = self.buffer1[0][0]
            self.left[0][1] = self.buffer1[0][1]
            self.left[0][2] = self.buffer1[0][2]
            
            self.buffer1 = copy.deepcopy(self.bottom)
            self.bottom[0][0] = self.buffer1[2][0]
            self.bottom[0][1] = self.buffer1[1][0]
            self.bottom[0][2] = self.buffer1[0][0]

            self.bottom[1][0] = self.buffer1[2][1]
            self.bottom[1][2] = self.buffer1[0][1]

            self.bottom[2][0] = self.buffer1[2][2]
            self.bottom[2][1] = self.buffer1[1][2]
            self.bottom[2][2] = self.buffer1[0][2]
        else:
            print "Invalid direction in rotate_bottom() method"

 ###################################################################################   
    def print_cube(self):
        print "     \t" + self.up[2][0] + " " + self.up[2][1] + " " + self.up[2][2] + "\n"
        print "     \t" + self.up[1][0] + " " + self.up[1][1] + " " + self.up[1][2] + "\n"
        print "     \t" + self.up[0][0] + " " + self.up[0][1] + " " + self.up[0][2] + "\n\n"
        print self.left[2][0] + " " + self.left[2][1] + " " + self.left[2][2] + "\t" + self.front[2][0] + " " + self.front[2][1] + " " + self.front[2][2] + "\t" + self.right[2][0] + " " + self.right[2][1] + " " + self.right[2][2] + "\t" + self.back[2][0] + " " + self.back[2][1] + " " + self.back[2][2] + "\n"
        print self.left[1][0] + " " + self.left[1][1] + " " + self.left[1][2] + "\t" + self.front[1][0] + " " + self.front[1][1] + " " + self.front[1][2] + "\t" + self.right[1][0] + " " + self.right[1][1] + " " + self.right[1][2] + "\t" + self.back[1][0] + " " + self.back[1][1] + " " + self.back[1][2] + "\n"
        print self.left[0][0] + " " + self.left[0][1] + " " + self.left[0][2] + "\t" + self.front[0][0] + " " + self.front[0][1] + " " + self.front[0][2] + "\t" + self.right[0][0] + " " + self.right[0][1] + " " + self.right[0][2] + "\t" + self.back[0][0] + " " + self.back[0][1] + " " + self.back[0][2] + "\n\n"
        print "     \t" + self.bottom[2][0] + " " + self.bottom[2][1] + " " + self.bottom[2][2] + "\n"
        print "     \t" + self.bottom[1][0] + " " + self.bottom[1][1] + " " + self.bottom[1][2] + "\n"
        print "     \t" + self.bottom[0][0] + " " + self.bottom[0][1] + " " + self.bottom[0][2] + "\n\n"
        
if __name__ == "__main__":
    r = Cube()




