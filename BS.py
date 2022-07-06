#Made by Aaron D'Cunha

#Imports
import random

class BattleShipAlg:

    _dir = ["up","down","left","right"]  
    
    grid = []
    emptyCell = "0"
    height = 0
    width = 0
    maxAttempts = 0
    gap = 0
    
    def __init__(self,_height, _width,char,gap=1,maxAttempt = 100):
        
        if _height < 3 or _width < 3 or gap < 0 or (gap > _width and gap > _height): raise Exception("Too small size or too huge gap")
        
        self.emptyCell = char
        self.height = _height
        self.width = _width
        self.maxAttempts = maxAttempt
        self.gap = gap
        
        #Creates an empty grid
        for _ in range(self.height):
            self._empty = []
            for _1 in range(self.width):
                self._empty.append(self.emptyCell)
                
            self.grid.append(self._empty)

    
    def printGrid(self):
        
        for _ in range(len(self.grid)):
            for _1 in range(len(self.grid[_])):
                print(self.grid[_][_1],end="")
            print("")
            
    def getPoint(self,x,y):
        
        return self.grid[y][x]
    
    def addShip(self,x,y,size,_direction,char):
        print(_direction)
        if _direction == "up":
            for _ in range((y-size),y):
                print(_,y)
                self.grid[_][x] = char
        elif _direction == "down":
            for _ in range(y,y+size):
                print(_,y)
                self.grid[_][x] = char
        elif _direction == "left":
            for _ in range((x-size),x):
                print(_,y)
                self.grid[y][_] = char
        elif _direction == "right":
            for _ in range(x,x+size):
               print(_,y)
               self.grid[y][_] = char
               
    def clamp(self,a,_min,_max):
        
        if a > _max: return _max
        if a < _min: return _min
        return a
    
    def genShips(self,size,char): #Size and Char are in the form of tuples. 
        
        
        random.shuffle(self._dir)
        
        while True:
            
            self.x = random.randint(0, self.width-1)
            self.y = random.randint(0,self.height-1)
            
            self.notWorking = False
            
            if self.x+self.gap > self.width or self.x-self.gap < 0 or self.y+self.gap > self.height or self.y-self.gap < 0:
                continue
            
            for d in self._dir:
                
                
                if d == "up":
                    
                    if self.y + 1 - size < 0 : continue
                    
                    for pointX in range(self.clamp((self.x-self.gap),0,(self.width-1)),self.clamp((self.x+self.gap),0,(self.width-1))):
                        for pointY in range(self.clamp((self.y-size+1-self.gap),0,(self.height-1)), self.clamp((self.y+1+self.gap),0,(self.height-1))):
                            if self.grid[pointY][pointX] != self.emptyCell:
                                self.notWorking = True
                                break
                    if self.notWorking:
                        self.notWorking = False
                        continue
                    else:
                        self.addShip(self.x, self.y, size, d, char)
                        break
                        
                elif d == "down":
                    
                    if self.y + size > self.height : continue
                    
                    for pointX in range( self.clamp((self.x-self.gap),0,(self.width-1))  ,  self.clamp((self.x+self.gap),0,(self.width-1))  ):
                        for pointY in range(self.clamp((self.y-self.gap),0,(self.height-1)), self.clamp((self.y+size+self.gap),0,(self.height-1))):
                            if self.grid[pointY][pointX] != self.emptyCell:
                                self.notWorking = True
                                break
                    if self.notWorking:
                        self.notWorking = False
                        continue
                    else:
                        self.addShip(self.x, self.y, size, d, char)
                        break
                        
                elif d == "left":
                    
                    if self.x + 1 - size < 0 : continue
                    
                    for pointX in range(self.clamp((self.x-size+1-self.gap),0,(self.width-1)), self.clamp((self.x+1+self.gap),0,(self.width-1))):
                        for pointY in range(self.clamp((self.y-self.gap),0,(self.height-1)),self.clamp((self.y+self.gap),0,(self.height-1))):
                            if self.grid[pointY][pointX] != self.emptyCell:
                                self.notWorking = True
                                break
                    if self.notWorking:
                        self.notWorking = False
                        continue
                    else:
                        self.addShip(self.x, self.y, size, d, char)
                        break
                        
                elif d == "right":
                    
                    if self.x + size > self.width : continue
                    
                    for pointX in range(self.clamp((self.x-self.gap),0,(self.width-1)), self.clamp((self.x+size+self.gap),0,(self.width-1))):
                        for pointY in range(self.clamp((self.y-self.gap),0,(self.height-1)),self.clamp((self.y+self.gap),0,(self.height-1))):
                            if self.grid[pointY][pointX] != self.emptyCell:
                                self.notWorking = True
                                break
                    if self.notWorking:
                        self.notWorking = False
                        continue
                    else:
                        self.addShip(self.x, self.y, size, d, char)
                        break
            if self.notWorking: continue
            else: break
            
        
        """for index in range(len(size)):
            
            random.shuffle(self._dir)
            
            self.canBuild = False
            
            for atmpt in range(self.maxAttempts):
               
                x = random.randint(0, self.width-1)
                y = random.randint(0,self.height-1)
                
                if x+self.gap > self.width or x-self.gap < 0 or y+self.gap > self.height or y-self.gap < 0:
                    continue
                
                for d in range(len(self._dir)):
                    
                    if self._dir[d] == "up":
                        
                        for pointX in range(x-self.gap,x+self.gap+1):
                            for pointY in range(y-self.height-self.gap+1,y+1+self.gap):
                                if self.getPoint(pointX,pointY) == self.emptyCell:
                                    self.canBuild = True
                                    self.addShip(x, y, size[d], self._dir[d], char[d])
                                    break
                            if self.canBuild : break
                        if self.canBuild : break
                    
                    if self._dir[d] == "down":
                        
                        for pointX in range(x-self.gap,x+self.gap+1):
                            for pointY in range(y-self.gap,y+self.height+self.gap):
                                if self.getPoint(pointX,pointY) == self.emptyCell:
                                    self.canBuild = True
                                    self.addShip(x, y, size[d], self._dir[d], char[d])
                                    break
                            if self.canBuild : break
                        if self.canBuild : break
                    
                    if self._dir[d] == "left":
                        
                        for pointX in range(x-self.width-self.gap+1,x+1+self.gap):
                            for pointY in range(y-self.gap,y+self.gap+1):
                                if self.getPoint(pointX,pointY) == self.emptyCell:
                                    self.canBuild = True
                                    self.addShip(x, y, size[d], self._dir[d], char[d])
                                    break
                            if self.canBuild : break
                        if self.canBuild : break
                    
                    if self._dir[d] == "right":
                        
                        for pointX in range(x-self.gap,x+self.width+self.gap):
                            for pointY in range(y-self.gap,y+self.gap+1):
                                if self.getPoint(pointX,pointY) == self.emptyCell:
                                    self.canBuild = True
                                    self.addShip(x, y, size[d], self._dir[d], char[d])
                                    break
                            if self.canBuild : break
                        if self.canBuild : break
                    
                    if d == len(self._dir - 1) or self.canBuild: break
                    
                if self.canBuild == False :
                    
                    continue
                    
                else:
                    break"""

                            
                            
                                
                                
                            
                            
                            
                            
                
    

emptyCell = "0"
grid = BattleShipAlg(10, 10, emptyCell)
size = [5,3,3,2]
char = ['5','3','3','2']
for i in range(len(size)):
    grid.genShips(size[i],char[i])
grid.printGrid()