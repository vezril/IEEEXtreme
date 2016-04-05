#!/usr/bin/env python
import sys


seq = 'AGT-'
l = len(seq)

def inc(seq, l, pos):
    seq = seq[::-1]

    posD = None

    # Find the last dash 
    for i in range(0,len(seq)):
        if seq[i] == '-':
            posD = i            
            
    if pos == None:
        sys.exit(0)
    
    # Find last character before the position of the dash to flip
    for i in range(0,posD):
        if seq[i] in ['A', 'T', 'G']:
            posD = i
            
    
