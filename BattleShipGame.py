#Made by Aaron D'Cunha

import random
#from os import system, name

class BS:
    
    #GameValues
    height = 10
    width = 10
    gap = 1
    direction = ['up','down','left','right']
    gameOver = False
    
    #Ships
    ship = [5,4,3,3,2]
    shipChar = ['A','B','C','D','E'] #Need to be unique
    shipHealth = ship.copy()
    shipPieces = 0
    
    #GridCharacters
    emptyCell = "O"
    sunkShip = "X"
    gridHor = ['-','A','B','C','D','E','F','G','H','I','J']
    gridVert = ['0','1','2','3','4','5','6','7','8','9']
    
    #Game Grid
    grid = []
    
    def __init__(self):
        #Creates Grid
        for i in range(self.height):
            w = []
            for _ in range(self.width):
                w.append(self.emptyCell)
            self.grid.append(w)
            
        self.generateLevel(self.ship, self.shipChar)
            
    def printGrid(self,hide = True):
        #Prints the Grid
        #Print the Horizontal Line Label
        for _ in self.gridHor: print(_,end="")
        print("")
        #Print each Horizontal Line + Vertical Label
        for _ in range(self.height):
            #Vertical Label
            print(self.gridVert[_],end="")
            for i in self.grid[_]:
                if i != self.emptyCell and i != self.sunkShip and hide:
                    print(self.emptyCell,end="") #Makes the ships hidden!
                else:
                    print(i,end="")
            print("")
            
    def addShip(self,pos,size,char,direction):
        #Adds the ship based on pos, size, character and direction given
        if direction == "up":
            for y in range(pos[1],pos[1]-(size-1) - 1,-1):
                self.grid[y][pos[0]] = char
        elif direction == "down":
            for y in range(pos[1],pos[1]+(size-1) + 1):
                self.grid[y][pos[0]] = char
        elif direction == "left":
            for x in range(pos[0],pos[0]-(size-1) - 1,-1):
                self.grid[x][pos[1]] = char
        elif direction == "right":
            for x in range(pos[0],pos[0]+(size-1) + 1):
                self.grid[pos[1]][x] = char
            
    def clamp(self,value,minimum,maximum):
        if value <= minimum: return minimum
        elif value >= maximum: return maximum
        else: return value
            
    def generateLevel(self,ships,chars):
        #Generates the Game Level
        for index in range(len(ships)):
            
            #Counts Turns
            turns = 0
            while True:
                
                #Iterate the turns
                turns += 1
                #Stops itself if it runs out of points to randomly choose
                if turns > self.height * self.width : break
                
                #Shuffles the direction list
                random.shuffle(self.direction)
                
                #Generates each ship by one by one
                x = random.randint(0,self.width-1)
                y = random.randint(0,self.height-1)
                
                #Checks if existing ship is in that position
                if self.grid[y][x] != self.emptyCell : continue
            
                chosenDir = None
            
                #Size Check
                for d in self.direction:
                    if d == "up":
                        if y-(ships[index]-1) >= 0 : chosenDir = d; break
                    if d == "down":
                        if y+(ships[index]-1) < self.height : chosenDir = d; break
                    if d == "left":
                        if x-(ships[index]-1) >= 0 : chosenDir = d; break
                    if d == "right":
                        if x+(ships[index]-1) < self.width : chosenDir = d; break
                    
                if chosenDir == None: continue
        
                #Gap/Valid Point Check
                if chosenDir == "up":
                    for pointX in range(self.clamp(x-self.gap,0,self.width-1),
                                        self.clamp(x+self.gap,0,self.width-1)+1):
                        for pointY in range(self.clamp(y-(ships[index]-1),0,self.height-1),
                                            self.clamp(y+self.gap,0,self.height-1)+1):
                            if self.grid[pointY][pointX] != self.emptyCell:
                                chosenDir = None
                                break
                        if chosenDir == None: break
                    
                elif chosenDir == "down":
                    for pointX in range(self.clamp(x-self.gap,0,self.width-1),
                                        self.clamp(x+self.gap,0,self.width-1)+1):
                        for pointY in range(self.clamp(y-self.gap,0,self.height-1),
                                            self.clamp(y+self.gap+(ships[index]-1),0,self.height-1)+1):
                            if self.grid[pointY][pointX] != self.emptyCell:
                                chosenDir = None
                                break
                        if chosenDir == None: break
                    
                elif chosenDir == "left":
                    for pointY in range(self.clamp(y-self.gap,0,self.height-1),
                                        self.clamp(y+self.gap,0,self.height-1)+1):
                        for pointX in range(self.clamp(x-(ships[index]-1),0,self.width-1),
                                            self.clamp(x+self.gap,0,self.width-1)+1):
                            if self.grid[pointY][pointX] != self.emptyCell:
                                chosenDir = None
                                break
                        if chosenDir == None: break
                    
                elif chosenDir == "right":
                    for pointY in range(self.clamp(y-self.gap,0,self.height-1),
                                        self.clamp(y+self.gap,0,self.height-1)+1):
                        for pointX in range(self.clamp(x-self.gap,0,self.width-1),
                                            self.clamp(x+self.gap+(ships[index]-1),0,self.width-1)+1):
                            if self.grid[pointY][pointX] != self.emptyCell:
                                print(self.grid[pointY][pointX],x,y,chosenDir,ships[index])
                                chosenDir = None
                                break
                        if chosenDir == None: break
                
                if chosenDir != None : 
                    self.shipPieces += ships[index]
                    self.addShip([x,y], ships[index], chars[index], chosenDir)
                    break
                
    def attackShip(self,pos):
        #Converts Labels to number position (Takes horizontal first and then vertical)
        position = [self.gridHor.index(pos[0])-1, self.gridVert.index(pos[1])]
        if self.grid[position[1]][position[0]] != self.emptyCell and self.grid[position[1]][position[0]] != self.sunkShip:
            self.shipHealth[self.shipChar.index(self.grid[position[1]][position[0]])] = self.shipHealth[self.shipChar.index(self.grid[position[1]][position[0]])] - 1
            self.grid[position[1]][position[0]] = self.sunkShip
            self.shipPieces -= 1
            if self.shipPieces <= 0 : self.gameOver = True
            
            return True
        else:
            return False
            
    def shipCount(self):
        count = 0
        for ship in self.shipHealth:
            if ship != 0: 
                count += 1
        return count

#Example Game
"""def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
      _ = system('clear')  
          
game = BS()
game.printGrid()
while game.gameOver == False:
    pos = input("Input Position (eg: A0): ")
    if pos.lower() == "show":
        clear()
        print("Ships Left:", game.shipCount())
        game.printGrid(False)
    else:

            clear()
            print([pos[0].capitalize(),pos[1]])
            if game.attackShip([pos[0].capitalize(),pos[1]]):
                print("HIT!")
            else:
                print("Miss!")
            print("Ships Left:", game.shipCount())
            game.printGrid()

        
print("Game Over")"""