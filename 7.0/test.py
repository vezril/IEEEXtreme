#!/usr/bin/env python
from itertools import permutations

#seq = [['AC', 'GG'],['AC-', 'G-G'],['A-C', 'GG-'],['-AC', 'GG-'],['AC-', '-GG'],['A-C', '-GG']]

x = permutations('AAAAABBBBCCCCCCCDDD')
v = []

while True:
    try:
        v.append(x.next())
    except:
        break

