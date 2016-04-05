#!/usr/bin/env python


def check(n):
    if n % 7 == 0:
        return True
    elif str(n).find('7') >=0:
        return True
    else:
        return False


class Student:
    def __init__(self, n=1, direction='+'):
        self.student_pos = n
        self.direction = direction
        self.hi = 1337
        self.lo = 1
        
    def inc(self):
        if self.direction == '+':
            if self.student_pos == self.hi:
                self.student_pos = self.lo
            else:
                self.student_pos += 1
        else:
            if self.student_pos == self.lo:
                self.student_pos = self.hi
            else:
                self.student_pos -= 1
        
    def toggle_direction(self):
        if self.direction == '+':
            self.direction = '-'
        else:
            self.direction = '+'

if __name__ == "__main__":

    n = int(raw_input())
    cases = []
    for i in range(0, n):
        cases.append(int(raw_input()))


    
    
    for j in range(0, n):
        s = Student()
        for i in range(1,cases[j]):
            if check(i):
                s.toggle_direction()
            s.inc()
        print s.student_pos
            
        
            
