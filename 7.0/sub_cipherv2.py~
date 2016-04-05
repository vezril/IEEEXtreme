#!/usr/bin/env python

def find_smallest(c):
    ml = 9999999999999999999
    s = None

    for key in c:
        if len(c[key]) < ml:
            s = key
    return key
    
class Sequence:
    def __init__(self, m=[]):
        self.cnt = 0
        self.m = m
        self. freq = {}
        
    def count_freq(self):
        self.m
        self.freq = {}
        self.cnt = 0;
        for key in self.m:
            for string in self.m[key]:
                for letter in string:
                    self.cnt +=1
                    try:
                        self.freq[letter] += 1
                    except:
                        self.freq[letter] = 1

      
class Decrypter:
    def __init__(self, p, c,cipher):
        self.c = c
        self.p = p
        # Cipher to Plain
        self.dc = {}
        # Plain to Cipher
        self.dp = {}
        self.cipher = cipher
        
        self.single()
        self.check()
        self.normalize()
        self.Decipher()       
    def isempty(self):
        return len(d.c.m) != 0
    
    def single(self):
        tkeys = []
        for key in self.p.m:
            if len(self.p.m[key]) == 1:
                for i in range(0, len(self.p.m[key][0])):
                    self    .dc[self.c.m[key][0][i]] = self.p.m[key][0][i]
                    self.dp[self.p.m[key][0][i]] = self.c.m[key][0][i]
                tkeys.append(key)
                
        for key in tkeys:
            del self.p.m[key]
            del self.c.m[key]
    
    def check(self):
        tkeys = []
        p = ''
        for key in self.c.m:
            for s in self.c.m[key]:
                for letter in s:
                    try:
                        p += self.dc[letter] 
                    except KeyError:
                        p = ''
                        break
                if len(p) > 0:
                    if len(self.c.m[key]) <= 1:
                        tkeys.append(key)
                    else:
                        self.c.m[key].remove(s)
                            
        for key in tkeys:
            try:
                del self.c.m[key]
            except:
                pass
                             
    def normalize(self):
        for key in self.dc:
            try:
                del self.c.freq[key.upper()]
            except:
                pass
                
        for key in self.dp:
            try:
                del self.p.freq[key.upper()]
            except:
                pass
            try:
                del self.p.freq[key.lower()]
            except:
                pass
                      
                
    def check_freq(self):
       recheck = False
       
    def guesswork(self):
        for key in self.c.m:
            for s in self.c.m[key]:
                p = ''
                for letter in s:
                    try:
                        p += d.dc[letter.upper()]
                    except:
                        p += letter
                    
                p = p.lower()                
                if len(p) == 2:
                    if p[0] == 't' or p[1] == 'o':
                        self.dc[self.c.m[key][0]] = 't'
                        self.dc[self.c.m[key][1]] = 'o'
                if len(p) == 3:
                    if (p[0] == 't' and p[1] == 'h') or (p[0] == 't' and p[2] == 'e') or (p[1] == 'h' and p[2] == 'e'):
                        self.dc[s[0]] = 't'
                        self.dc[s[1]] = 'h'
                        self.dc[s[2]] = 'e'
                        p = 'the'
                    else:
                        pass
                if len(self.c.m[key]) == 1:
                    
                    del self.c.m[key]
                    del self.p.m[key]
                else:
                    self.c.m[key].remove(s)
                    self.p.m[key].remove(p)
 
       
    def Decipher(self):
        self.plaintext = ''
        for letter in self.cipher:
            try:
                self.plaintext += self.dc[letter]
            except:
                self.plaintext += letter
                
                

if __name__ == "__main__":

    freq = { 'a':0.8167, 'b':0.1492, 'c':0.2782, 'd':0.4253, 'e':0.12702, 'f':0.2228, 'g':0.2015, 'h':0.6094, 'i':0.6966, 'j':0.0153, 'k':0.0772,'l':0.4025,'m':0.2406,'n':0.6749,'o':0.7507,'p':0.1929,'q':0.0095,'r':0.5987,'s':0.6327,'t':0.9056,'u':0.2758,'v':0.0978,'w':0.2360,'x':0.0150,'y':0.1974,'z':0.0074}
        
        
            
    N = int(raw_input())
    #pt = ['ball','belongs', 'red', 'the', 'to']
    #ct = ['SJI', 'XIL', 'TEMM', 'TIMUBPK', 'SU', 'ETI']
    pt = []
    ct = []
    for i in range(0,N):
        pt.append(raw_input().strip())
        
    raw_input()
    ciphermeh = raw_input().strip()
    ct = ciphermeh.split(' ')

    p = {}
    c = {}
    for plain in pt:
        try:
            p[len(plain)].append(plain)
        except:
            p[len(plain)] = [plain]
            
    for cipher in ct:
        try:
            c[len(cipher)].append(cipher)
        except:
            c[len(cipher)] = [cipher]            
            
    cipher = Sequence(c)        
    plain = Sequence(p)
            
            
    cipher.count_freq()
    plain.count_freq()
    
    d = Decrypter(plain, cipher,ciphermeh)
    
    
    while d.isempty():
        d.single()
        d.check()
        d.normalize()
        d.guesswork()
        d.Decipher
    
    d.Decipher()
    print d.plaintext.upper()
