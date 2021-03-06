#!/usr/bin/env python
from copy import deepcopy
import sys

class Path:
    def __init__(self):
        self.list = []
        self.score = 0
        
def CalculateR(mountain, path):
    r = 0
    for coordinate in path:
        
       # print coordinate[0]
       # print coordinate[1]
        r+=mountain[coordinate[0]][coordinate[1]]
        
    return r

def find(mountain, path, row, col):
    # Check extremities
    # If extremities, ignore this path <<------------
    if col < 0 or col > len(mountain[row])-1:
        return path
        
    # mountain was found    
    if row == 0:

        pathOriginal = deepcopy(path) 
        pathOriginal.append((row,col))
        return pathOriginal
        
    pathOriginal = deepcopy(path)  
    pathOriginal.append((row,col))

    
    r1 = find(mountain, pathOriginal, row-1, col-1)
    r2 = find(mountain, pathOriginal, row-1, col)
    r3 = find(mountain, pathOriginal, row-1, col+1)
    


    if len(r1) != len(mountain):
        eval_r1 = -1
    else:
        eval_r1 = CalculateR(mountain, r1)
        
    if len(r2) != len(mountain):
        eval_r2 = -1
    else:
        eval_r2 = CalculateR(mountain, r2)
        
    if len(r3) != len(mountain):
        eval_r3 = -1
    else:
        eval_r3 = CalculateR(mountain, r3)
        
    try:
        if mountain[row-1,col-1] == mountain[row-1,col]:
            eval_r2 = -1
    except:    
        pass
    
    try:        
        if mountain[row-1,col-1] == mountain[row-1,col+1]:
            eval_r3 = -1
    except:    
        pass

    try:
        if mountain[row-1,col] == mountain[row-1,col+1]:
            eval_r3 = -1
    except:    
        pass
       
    tmp = [(eval_r1, r1), (eval_r2,r2), (eval_r3,r3)]
    l = []
    for n in tmp:
        if n[0] != -1:
            l.append(n)
            
    #print l        
    minv = (9999999999999999999999999999999999999999999999999999999999, r1)
    for n in l:
        if minv[0] > n[0]:
            minv = n
    
    return minv[1]

def format_tuple(t):
    return '[' + str(t[0]) + ',' + str(t[1]) + ']'

'''
7 7
2 2 2 1 2 3 4 
2 2 1 2 1 2 5
4 1 1 2 1 1 5 
1 2 2 3 3 4 1 
4 1 1 2 2 1 4
3 4 1 4 1 2 1
1 2 1 1 1 2 1
'''

if __name__ == "__main__":    
    mountain = [[2,2,2,1,2,3,4],[2,2,1,2,1,2,5],[4,1,1,2,1,1,5],[1,2,2,3,3,4,1],[4,1,1,2,2,1,4],[3,4,1,4,1,2,1],[1,2,1,1,1,2,1]]    
    rowCol = (raw_input()).split(' ')
    row = int(rowCol[0])
    col = int(rowCol[1])

    mountain = [[0 for x in xrange(col)] for x in xrange(row)]


    for i in range(0,row):
        string = raw_input()
        string = string.strip().split(' ')
        for j in range(0, len(string)):
            mountain[i][j] = int(string[j])  
        
  
    #print find(mountain, [], row-1,col-1)    
    path = []
    for i in range(0,col):
        path.append((find(mountain, [],row-1,i)))


    #print find(mountain, [],row-1,i)
    p = path.pop()
    m = CalculateR(mountain, p)
    saved = p
    for p in path:
        tmp = CalculateR(mountain, p)
        if tmp < m:
            saved = p
            m = tmp
    saved = saved[::-1]
    
    out = 'Minimum risk path = ' 
    for t in saved:
        out += format_tuple(t)    
        
    print out
    print 'Risks along the path = ' + str(m)
        
        
        
        
        
