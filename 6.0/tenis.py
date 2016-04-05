#!/usr/bin/env python2.6
import fileinput,sys,os,copy

def print_grid(grid,row,col):
    for n in range(0,row):
        print "n" + str(n) + "| " + str(grid[n])

def get_pos_r1(grid):
    row = grid[0]
    for n in range(0, len(row)):
        if row[n] == '1':
            return (0,n)

def get_pos_r2(grid):
    row = grid[-1]
    for n in range(0, len(row)):
        if row[n] == '2':
            return (len(grid)-1,n)

def get_robot_pos(grid):
    return [get_pos_r1(grid),get_pos_r2(grid)]

def check_colision(robots,ball_pos,objs,grid,cols,rows):

    # Check Edges
    if((ball_pos[0] == 0) or (ball_pos[1] == 0) or (ball_pos[1] == cols) or (ball_pos[0] == rows)):

        return True
    # Check Robot
    if((robots[0] == ball_pos) or (robots[1] == ball_pos)):
        return False

    # Check Objects
    for n in range(0,len(objs)):
        if(objs[n] == ball_pos):
            return True
    return False

if __name__ == "__main__":
    # Gride Size
    #4,4
    #rows = 4
    #cols = 4
    tmp = raw_input()
    (rows,cols) = tmp.split(',')
    rows = int(rows)
    cols = int(cols)
    # Init pos of Robot1
    #0
    #r1_pos = 0
    r1_pos = raw_input()
    r1_pos = int(r1_pos)
    #3
    #r2_pos = 3
    r2_pos = raw_input()
    r2_pos = int(r2_pos)
    # if 1 -> robot1 has the ball, if 2 -> robog2
    #ball_start = 1
    ball_start = raw_input()
    ball_start = int(ball_start)
    ball_vector = ''

    # Num of obstacles
    #1
    #num_ob = 1
    num_ob = raw_input()
    num_ob = int(num_ob)
    # Position of obs ob_row,ob_col
    ob_pos = []
    for n in range(0,num_ob):
        tmp = raw_input()
        tmp2 = tmp.split(',')
        ob_pos.append((int(tmp2[0]),int(tmp2[1])))

    # Moves
    #LLRSLRSSR
    #moves = 'LLRSLRSSR'
    moves = raw_input()
    moves = moves.upper()
    move_r1 = copy.deepcopy(moves)
    move_r2 = copy.deepcopy(moves)
    move_r2 = move_r2.lower()
    move_tot = ''
    grid = []

    for n in range(0,rows):
        row = []
        for m in range(0,cols):
            row.append('E')
        grid.append(row)

    for n in range(0,num_ob):
        obj = ob_pos[n]
        #grid[obj[0]][obj[1]] = 'O'

    grid[0][r1_pos] = '1'
    grid[rows-1][r2_pos] = '2'

    if(ball_start == 1):
        #rob1
        ball_pos = (0,r1_pos)
    elif(ball_start == 2):
        ball_pos = (cols-1,r2_pos)
    else:
        sys.exit(0)

    while True:
        #print_grid(grid,rows,cols)
        robot_pos = get_robot_pos(grid)
        # Check if robot has ball    
        if(robot_pos[0] == ball_pos):
            ball_vector = move_r1[0]
            move_r1 = move_r1[1:]
            move_tot = move_tot + ball_vector
            if(len(move_r1) == 0):
                move_r1 = copy.deepcopy(moves)
  
        elif(robot_pos[1] == ball_pos):
            ball_vector = move_r1[0]
            move_r1 = move_r1[1:]
            move_tot = move_tot + ball_vector
            if(len(move_r1) == 0):
                move_r1 = copy.deepcopy(moves)
                move_r1 = move_r1.lower()


        # Move ball
       # print "Ball Vector: " + ball_vector
        if((ball_pos == (0,0)) or (ball_pos == (0,cols-1)) or (ball_pos == (rows-1,0)) or (ball_pos == (rows-1,cols-1))):
            if(ball_vector == 'L'):
                ball_vector = 'R'
            elif(ball_vector == 'R'):
                ball_vector = 'L'
            elif(ball_vector == 'l'):
                ball_vector = 'r'
            elif(ball_vector == 'r'):
                ball_vector = 'l'
            else:
                if(ball_vector.islower()):
                    ball_vector = ball_vector.upper()
                else:
                    ball_vector = ball_vector.lower()
        elif(check_colision(robot_pos,ball_pos, ob_pos,grid,cols,rows)):
            if(ball_vector == 'L'):
                ball_vector = 'R'
            elif(ball_vector == 'R'):
                ball_vector = 'L'
            elif(ball_vector == 'l'):
                ball_vector = 'r'
            elif(ball_vector == 'r'):
                ball_vector ='l'
            else:
                if(ball_vector.islower()):
                    ball_vector = ball_vector.upper()
                else:
                    ball_vector = ball_vector.lower()
        if(ball_vector == 'L'):
            ball_pos = (ball_pos[0]+1,ball_pos[1]-1)
        elif(ball_vector == 'l'):
            ball_pos = (ball_pos[0]-1,ball_pos[1]-1)
        elif(ball_vector == 'R'):
            ball_pos = (ball_pos[0]+1,ball_pos[1]+1)
        elif(ball_vector == 'r'):
            ball_pos = (ball_pos[0]-1,ball_pos[1]+1)
        elif(ball_vector == 'S'):
            ball_pos = (ball_pos[0]+1,ball_pos[1])
        elif(ball_vector == 's'):
            ball_pos = (ball_pos[0]-1,ball_pos[1])

        # Move Robot
        # Robot 1
        robot = robot_pos[0]
        if(robot[1] > ball_pos[1]):
            if((robot[1] == 0)):
                robot = (0,robot[1]+1)
            else:
                robot = (0,robot[1]-1)
        elif(robot[1] < ball_pos[1]):
            if((robot[1] == cols-1)):
                robot = (0,robot[1]-1)
            else:
                robot = (0,robot[1]+1)
        else:
            if(robot[1] == cols-1):
                robot = (0,robot[1]-1)
            elif(robot[1] == 0):
                robot = (0,robot[1]+1)
            else:
                robot = (0,robot[1]+1)

        grid[0][robot_pos[0][1]] = 'E'
        grid[0][robot[1]] = '1'
        # Robot 2
        robot = robot_pos[1]
        if(robot[1] > ball_pos[1]):
            if((robot[1] == 0)):
                robot = (rows-1,robot[1]+1)
            else:
                robot = (rows-1,robot[1]-1)
        elif(robot[1] < ball_pos[1]):
            if((robot[1] == cols-1)):
                robot = (rows-1,robot[1]-1)
            else:
                robot = (rows-1,robot[1]+1)
        else:
            if(robot[1] == cols-1):
                robot = (rows-1,robot[1]-1)
            elif(robot[1] == 0):
                robot = (rows-1,robot[1]+1)
            else:
                robot = (rows-1,robot[1]+1)
        grid[rows-1][robot_pos[1][1]] = 'E'
        grid[rows-1][robot[1]] = '2'
        
        # Check if lost
        robot_pos = get_robot_pos(grid)

        if(ball_pos != robot_pos[0]) and (ball_pos[0] == 0):
            lose = 1
            break
        elif(ball_pos != robot_pos[1]) and (ball_pos[0] == rows-1):
            lose = 2
            break

    #print "Ball: (" + str(ball_pos[0]) + ',' + str(ball_pos[1]) + ")"  
    #print "Ball: (" + str(ball_pos[0]) + ',' + str(ball_pos[1]) + ")"
    #print_grid(grid,rows,cols)
    #print "Lost: " + str(lose)
    robots = get_robot_pos(grid)
    if(lose != 1):
        print "Winner: Robot1"
    else:
        print "Winner: Robot2"

    print "Robot1 At [" + str(robots[0][0]) + "," + str(robots[0][1]) + "]"
    print "Robot2 At [" + str(robots[1][0]) + "," + str(robots[1][1]) + "]"
    print "Ball At [" + str(ball_pos[0]) + "," + str(ball_pos[1]) + "]"
    #print "Sequence: " + ball_vector.upper()	
    print "Sequence: " + move_tot.upper()

#
