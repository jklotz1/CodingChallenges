from Direction import *

#class definition of Spiral class
#  current x,y position when filling in the spiral
#  array that gets filled in
#  the next value that will fill the spiral in
#  n is the boundary
#  direction is the current direction to move in the spiral
class Spiral():
    x = 0 
    y = 0
    array = []
    value = 1
    n = 0
    direction = ""
    
    def __init__(self, _n):
        self.n = _n
        #sets base empty array
        self.array = [[0 for i in range(self.n)] for j in range(self.n)]
        #sets initial direction
        self.direction = RightDirection()
        
    #checks to see if the x or y values exceeds the boundary n
    #used as a breaking condition
    def checkBoundaries(self):
        return (self.direction.checkLocation(self) 
                and self.array[self.x][self.y] == 0)       
    
    #gets the next direction object
    #the next direction to move in the spiral
    def getNextDirectionInstance(self):
        return {
            1 : RightDirection(),
            2 : DownDirection(),
            3 : LeftDirection(),
            0 : UpDirection()
        }[self.direction.currentDirection] 
    
    #gets the index of the next direction to move in the spiral
    def getNextDirection(self):
        self.direction.getNextDirection()
        self.direction = self.getNextDirectionInstance() 
        
    #Fill in spiral moving in the direction stored in spiral
    def fillArray(self):
        #sets starting coordinates and values in spiral
        x = self.x
        y = self.y
        value = self.value
        move = self.direction.getDisplacement()
        
        #fill in spiral until all values are filled
        #uses the function defintion depending on distance object
        #continues in spiral directions (right, down, left, up,...) until done
        #loop breaks when all values are filled in or boundaries are hit
        while (self.checkBoundaries()):
            self.array[self.x][self.y] = value
            self.x += move[0]
            self.y += move[1]
            value += 1  
            if (not self.checkBoundaries()):
                self.x -= move[0]
                self.y -= move[1]
                self.getNextDirection()
                self.direction.getStartCoordinates(self)
                move = self.direction.getDisplacement()
        return self    
        