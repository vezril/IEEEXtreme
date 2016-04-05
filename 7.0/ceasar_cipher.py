#!/usr/bin/env python

class Cipher:
    def __init__(self, cipher, dictionary):
        self.k1 = None
        self.k2 = None
        self.k3 = None
        self.blockL = None
        self.cipher = cipher
        self.dictionary = dictionary
        self.hi = 0
        self.decoded = ''
        
        for val in self.dictionary:
            if len(val) > self.hi:
                self.hi = len(val)
                
    def rotate(self, n, x):
        def shift(c, x):
            if x == 0:
                return c
            else:
                if ord(c) >= 90:
                    c = 'A'
                else:
                    c = chr(ord(c)+1)
                return shift(c,x-1)
    
    
        rot = ''
        for character in n:
            rot += shift(character, x)
        return rot

    
    def Decipher(self):
        bl = 2
        lo = 0
        hi = lo + bl
        flag = False
        self.decoded = ''
        while bl < 6:
            while hi < len(self.cipher):
                for i in range(0,26):
                    s = self.rotate(self.cipher[lo:hi],i)
                    

                        
                        
                        
                    flag = True
                if flag == True:
                    bl = 9999
                    break
                lo += 1
                hi += 1
            bl+=1
            lo = 0
            hi = lo+bl
                 
                    
        
        
    def findBlockLength(self):
        lo = 0
        hi = 5
        flag = False
        rotv = 0

        while hi < len(self.cipher):
            for i in range(0,26):
                decrypt = self.rotate(self.cipher[lo:hi], i)
                #print decrypt
                if decrypt in self.dictionary:
                    flag = True
                    break
            if flag == True:
                break
                    
            hi +=1
            lo +=1
        rotv = i
        
        print self.rotate(self.cipher[lo:hi],i)
        print '''
        I:  %i
        LO: %i
        HI: %i
        ''' % (i, lo, hi)
            



if __name__ == "__main__":

    dictionary = ['A', 'ABLE', 'ABOUT', 'ABOVE', 'ACT', 'ADD', 'ADVANCING', 'AFTER', 'AGAIN', 'AGAINST', 'AGE', 'AGO', 'AIR', 'ALL', 'ALSO', 'ALWAYS', 'AM', 'AN', 'AND', 'ANIMAL', 'ANSWER', 'ANY', 'APPEAR', 'ARE', 'AREA', 'AS', 'ASK', 'ASSOCIATION', 'AT', 'ATTACK', 'BACK', 'BASE', 'BE', 'BEAUTY', 'BEEN', 'BEFORE', 'BEGAN', 'BEGIN', 'BEHIND', 'BENEFIT', 'BEST', 'BETTER', 'BETWEEN', 'BIG', 'BIRD', 'BLACK', 'BLUE', 'BOAT', 'BODY', 'BOOK', 'BOTH', 'BOX', 'BOY', 'BROUGHT', 'BUILD', 'BUSY', 'BUT', 'BY', 'CALL', 'CAME', 'CAN', 'CAR', 'CARE', 'CARRY', 'CAUSE', 'CENTER', 'CERTAIN', 'CHANGE', 'CHECK', 'CHILDREN', 'CITY', 'CLASS', 'CLEAR', 'CLOSE', 'COLD', 'COLOR', 'COME', 'COMMON', 'COMPLETE', 'CONTAIN', 'CORRECT', 'COULD', 'COUNTRY', 'COURSE', 'COVER', 'CROSS', 'CRY', 'CUT', 'DARK', 'DAY', 'DECIDE', 'DEDICATED', 'DEEP', 'DEVELOP', 'DID', 'DIFFER', 'DIRECT', 'DO', 'DOES', 'DOG', 'DONT', 'DONE', 'DOOR', 'DOWN', 'DRAW', 'DRIVE', 'DRY', 'DURING', 'EACH', 'EARLY', 'EARTH', 'EASE', 'EAT', 'END', 'ENOUGH', 'EVEN', 'EVER', 'EVERY', 'EXAMPLE', 'EXCELLENCE', 'EYE', 'FACE', 'FACT', 'FALL', 'FAMILY', 'FAR', 'FARM', 'FAST', 'FATHER', 'FEEL', 'FEET', 'FEW', 'FIELD', 'FIGURE', 'FINAL', 'FIND', 'FINE', 'FIRE', 'FIRST', 'FISH', 'FIVE', 'FLY', 'FOLLOW', 'FOOD', 'FOOT', 'FOR', 'FORCE', 'FORM', 'FOUND', 'FOUR', 'FREE', 'FRIEND', 'FROM', 'FRONT', 'FULL', 'GAME', 'GAVE', 'GET', 'GIRL', 'GIVE', 'GO', 'GOLD', 'GOOD', 'GOT', 'GOVERN', 'GREAT', 'GREEN', 'GROUND', 'GROUP', 'GROW', 'HAD', 'HALF', 'HAND', 'HAPPEN', 'HARD', 'HAS', 'HAVE', 'HE', 'HEAD', 'HEAR', 'HEARD', 'HELP', 'HER', 'HERE', 'HIGHHIM', 'HIS', 'HOLD', 'HOME', 'HORSE', 'HOT', 'HOUR', 'HOUSE', 'HOW', 'HUMANITY', 'HUNDRED', 'I', 'IDEA', 'IEEE', 'IF', 'IN', 'INCH', 'INNOVATION', 'INTEREST', 'IS', 'ISLAND', 'IT', 'JUST', 'KEEP', 'KIND', 'KING', 'KNEW', 'KNOW', 'LAND', 'LARGE', 'LARGEST', 'LAST', 'LATE', 'LAUGH', 'LAY', 'LEAD', 'LEARN', 'LEAVE', 'LEFT', 'LESS', 'LET', 'LETTER', 'LIFE', 'LIGHT', 'LIKE', 'LINE', 'LIST', 'LISTEN', 'LITTLE', 'LIVE', 'LONG', 'LOOK', 'LOT', 'LOVE', 'LOW', 'MACHINE', 'MADE', 'MAIN', 'MAKE', 'MAN', 'MANY', 'MAP', 'MARK', 'MAY', 'ME', 'MEAN', 'MEASURE', 'MEN', 'MIGHT', 'MILE', 'MIND', 'MINUTE', 'MISS', 'MONEY', 'MOON', 'MORE', 'MORNING', 'MOST', 'MOTHER', 'MOUNTAIN', 'MOVE', 'MUCH', 'MUSIC', 'MUST', 'MY', 'NAME', 'NEAR', 'NEED', 'NEVER', 'NEW', 'NEXT', 'NIGHT', 'NO', 'NORTH', 'NOTE', 'NOTHING', 'NOTICE', 'NOUN', 'NOW', 'NUMBER', 'NUMERAL', 'OBJECT', 'OF', 'OFF', 'OFTEN', 'OH', 'OLD', 'ON', 'ONCE', 'ONE', 'ONLY', 'OPEN', 'OR', 'ORDER', 'OTHER', 'OUR', 'OUT', 'OVER', 'OWN', 'PAGE', 'PAPER', 'PART', 'PASS', 'PATTERN', 'PEOPLE', 'PERSON', 'PICTURE', 'PIECE', 'PLACE', 'PLAIN', 'PLAN', 'PLANE', 'PLANT', 'PLAY', 'POINT', 'PORT', 'POSE', 'POSSIBLE', 'POUND', 'POWER', 'PRESS', 'PROBLEM', 'PRODUCE', 'PRODUCT', 'PROFESSIONAL', 'PULL', 'PUT', 'QUESTION', 'QUICK', 'RAIN', 'RAN', 'REACH', 'READ', 'READY', 'REAL', 'RECORD', 'RED', 'REMEMBER', 'REST', 'RIGHT', 'RIVER', 'ROAD', 'ROCK', 'ROOM', 'ROUND', 'RULE', 'RUN', 'SAID', 'SAME', 'SAW', 'SAY', 'SCHOOL', 'SCIENCE', 'SEA', 'SECOND', 'SEE', 'SEEM', 'SELF', 'SENTENCE', 'SERVE', 'SET', 'SEVERAL', 'SHE', 'SHIP', 'SHORT', 'SHOULD', 'SHOW', 'SIDE', 'SIMPLE', 'SINCE', 'SING', 'SIX', 'SIZE', 'SLEEP', 'SLOW', 'SMALL', 'SO', 'SOME', 'SONG', 'SOON', 'SOUND', 'SOUTH', 'SPECIAL', 'SPELL', 'STAND', 'STAR', 'START', 'STATE', 'STAY', 'STEP', 'STILL', 'STOOD', 'STOP', 'STORY', 'STREET', 'STRONG', 'STUDY', 'SUCH', 'SUN', 'SURE', 'SURFACE', 'TABLE', 'TAIL', 'TAKE', 'TALK', 'TEACH', 'TECHNOLOGICAL', 'TELL', 'TEN', 'TEST', 'THAN', 'THAT', 'THE', 'THEIR', 'THEM', 'THEN', 'THERE', 'THESE', 'THEY', 'THING', 'THINK', 'THIS', 'THOSE', 'THOUGH', 'THOUGHT', 'THOUSAND', 'THREE', 'THROUGH', 'TIME', 'TO', 'TOGETHER', 'TOLD', 'TOO', 'TOOK', 'TOP', 'TOWARD', 'TOWN', 'TRAVEL', 'TREE', 'TRUE', 'TRY', 'TURN', 'TWO', 'UNDER', 'UNIT', 'UNTIL', 'UP', 'US', 'USE', 'USUAL', 'VERY', 'VOICE', 'VOWEL', 'WAIT', 'WALK', 'WANT', 'WAR', 'WARM', 'WAS', 'WATCH', 'WATER', 'WAY', 'WE', 'WEBSITE', 'WEEK', 'WELL', 'WENT', 'WERE', 'WEST', 'WHAT', 'WHEEL', 'WHEN', 'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHO', 'WHOLE', 'WHY', 'WILL', 'WIND', 'WITH', 'WONDER', 'WOOD', 'WORD', 'WORK', 'WORLD', 'WORLDS', 'WOULD', 'WRITE', 'YEAR', 'YET', 'YOU', 'YOUNG', 'YOUR']

    
    #print dictionary
    ins = 'ZVVVZBCQNFJMGYNCRIXVBCYAXAZNNDFERCRBBXLRVODJIUVUZTJCNMCJVYQVETZEXCNLQWJGJBDTRCZEWXEJCDJIVIUVOTVUUNWLZAJMOYVSVENORCXACPHVEZKPCNCDBYGVIOJRKKRTTCQNRZZZRZSJZK'
    
    
    c = Cipher(ins, dictionary)
    
    
    c.findBlockLength()
