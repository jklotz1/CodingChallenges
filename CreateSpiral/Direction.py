#defintion parent class Direction
#  holds the index of the current direction to move in the spiral
class Direction:
    currentDirection = 0
    
    def __init__(self):
        self.data = []   
    
    #gets the index of the next direction to move in the spiral
    def getNextDirection(self):
        self.currentDirection = (self.currentDirection + 1) % 4
    
#defintion of RightDirection, inherits from Direction
#contains actions specific to moving right to fill in spiral
class RightDirection(Direction):
    currentDirection = 1
    
    #Returns the vector of change for moving in the right direction
    def getDisplacement(self):
        return [0,1]
    
    #checks to see if the coordinates are out of bounds
    def checkLocation(self, spiral):
        return (spiral.y < spiral.n)
    
    #shifts starting coordinates to new starting spot
    def getStartCoordinates(self, spiral):
        spiral.y += 1
        return spiral
            
#defintion of DownDirection, inherits from Direction
#contains actions specific to moving down to fill in spiral    
class DownDirection(Direction):
    currentDirection = 2

    #Returns the vector of change for moving in the down direction
    def getDisplacement(self):
        return [1,0]   
    
    #checks to see if the coordinates are out of bounds
    def checkLocation(self, spiral):
        return (spiral.x < spiral.n)    
    
    #shifts starting coordinates to new starting spot
    def getStartCoordinates(self, spiral):
        spiral.x += 1
        return spiral    
        
#defintion of LeftDirection, inherits from Direction
#contains actions specific to moving left to fill in spiral
class LeftDirection(Direction):
    currentDirection = 3
    
    #Returns the vector of change for moving in the left direction
    def getDisplacement(self):
        return [0,-1]  
    
    #checks to see if the coordinates are out of bounds
    def checkLocation(self, spiral):
        return (spiral.y >= 0)     
    
    #shifts starting coordinates to new starting spot
    def getStartCoordinates(self, spiral):
        spiral.y -= 1
        return spiral     

#defintion of UpDirection, inherits from Direction
#contains actions specific to moving up to fill in spiral
class UpDirection(Direction):
    currentDirection = 0
    
    #Returns the vector of change for moving in the down direction
    def getDisplacement(self):
        return [-1,0]  
    
    #checks to see if the coordinates are out of bounds
    def checkLocation(self, spiral):
        return (spiral.x >= 0)     
    
    #shifts starting coordinates to new starting spot
    def getStartCoordinates(self, spiral):
        spiral.x -= 1
        return spiral  