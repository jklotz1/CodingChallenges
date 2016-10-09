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
    
    #Fill in spiral moving in the right direction
    #takes in spiral object for filling in
    def fillArray(self, spiral):
        #sets starting coordinates and values in spiral
        x = spiral.x
        y = spiral.y
        value = spiral.value
        
        #fill in array until edge or a space that is already filled
        while (y < spiral.n and spiral.array[x][y] == 0):
            spiral.array[x][y] = value
            y += 1
            value += 1
        spiral.y = y - 1
        spiral.value = value
        return spiral
    
    #shifts starting coordinates to new starting spot
    def getStartCoordinates(self, spiral):
        spiral.y += 1
        return spiral
            
#defintion of DownDirection, inherits from Direction
#contains actions specific to moving down to fill in spiral    
class DownDirection(Direction):
    currentDirection = 2
    
    #Fill in spiral moving in the down direction
    #takes in spiral object for filling in    
    def fillArray(self, spiral):
        #sets starting coordinates and values in spiral
        x = spiral.x
        y = spiral.y
        value = spiral.value
        
        #fill in array until edge or a space that is already filled
        while (x < spiral.n and spiral.array[x][y] == 0):
            spiral.array[x][y] = value
            x += 1
            value += 1
            
        spiral.x = x - 1
        spiral.value = value
        return spiral
    
    #shifts starting coordinates to new starting spot
    def getStartCoordinates(self, spiral):
        spiral.x += 1
        return spiral    
        
#defintion of LeftDirection, inherits from Direction
#contains actions specific to moving left to fill in spiral
class LeftDirection(Direction):
    currentDirection = 3
    
    #Fill in spiral moving in the left direction
    #takes in spiral object for filling in    
    def fillArray(self, spiral):
        #sets starting coordinates and values in spiral
        x = spiral.x
        y = spiral.y
        value = spiral.value
        
        #fill in array until edge or a space that is already filled
        while (y >= 0 and spiral.array[x][y] == 0):
            spiral.array[x][y] = value
            y -= 1
            value += 1
            
        spiral.y = y + 1
        spiral.value = value
        return spiral
    
    #shifts starting coordinates to new starting spot
    def getStartCoordinates(self, spiral):
        spiral.y -= 1
        return spiral     

#defintion of UpDirection, inherits from Direction
#contains actions specific to moving up to fill in spiral
class UpDirection(Direction):
    currentDirection = 0
    
    #Fill in spiral moving in the up direction
    #takes in spiral object for filling in    
    def fillArray(self, spiral):
        #sets starting coordinates and values in spiral
        x = spiral.x
        y = spiral.y
        value = spiral.value
        
        #fill in array until edge or a space that is already filled
        while (x >= 0 and spiral.array[x][y] == 0):
            spiral.array[x][y] = value
            x -= 1
            value += 1
            
        spiral.x = x + 1
        spiral.value = value
        return spiral
    
    #shifts starting coordinates to new starting spot
    def getStartCoordinates(self, spiral):
        spiral.x -= 1
        return spiral  