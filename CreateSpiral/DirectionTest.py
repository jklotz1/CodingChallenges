from Direction import *
from Spiral import *

#verify that the function output matches the expected output
def verifyFunctionOutput(functionOutput, expectedOutput):
    return (functionOutput == expectedOutput)

def testGetNextDirection(d, expected, direction):
    print("when currentDirection = " + str(d.currentDirection) + " for " 
          + direction)
    print('getNextDirection() results in currentDirection == ' 
          + str(expected))
    d.getNextDirection()
    print("Result: " + str(verifyFunctionOutput(d.currentDirection, 
                                                expected))) 

def testGetDisplacement(d, direction, expected):
    print("getDisplacement() for " + direction 
          + "Direction results in " + str(expected))
    print("Result: " + str(verifyFunctionOutput(d.getDisplacement(), 
                                                expected)))
    
def testCheckLocation(d, s, expected, direction):
    print("when current coordinates = " + str([s.x,s.y]) + " and n = " 
          + str(s.n))   
    print("checkLocation() for " + direction 
          + "Direction results in " + str(expected))
    print("Result: " + str(verifyFunctionOutput(d.checkLocation(s), 
                                                expected)))    

def testGetStartCoordinates(s, d, expected, direction):
    print("when current coordinates = " + str([s.x,s.y]))   
    d.getStartCoordinates(s)
    print("getStartCoordinates() for " + direction 
          + "Direction results in " + str(expected))
    print("Result: " + str(verifyFunctionOutput([s.x,s.y], expected))) 
    

#test function of base class: getNextDirection()
def verifyGetNextDirection():
    #start with base class
    #check value after two calls to the function
    d = Direction()
    testGetNextDirection(d, 1, "Direction()")
    testGetNextDirection(d, 2, "Direction()")
    
    #verify with subclass
    #RightDirection sets currentDirection = 1
    d = RightDirection()
    testGetNextDirection(d, 2, "RightDirection()")
    testGetNextDirection(d, 3, "RightDirection()")      
    
def verifyGetDisplacement():
    #check the value return for each direction subclass
    d = RightDirection()
    testGetDisplacement(d, "Right", [0,1])
    d = DownDirection()
    testGetDisplacement(d, "Down", [1,0])
    d = LeftDirection()
    testGetDisplacement(d, "Left", [0,-1])
    d = UpDirection()
    testGetDisplacement(d, "Up", [-1,0])   
    
def verifyCheckLocation():
    #check the value return by testLocation for each subclass
    #RightDirection subclass
    d = RightDirection()
    s = Spiral(3)
    #x and y are both 1 to begin which is valid
    testCheckLocation(d,s,True,"Right")
    #update coordinates to outside boundary
    s.y = 3
    testCheckLocation(d,s,False, "Right")
    
    #DownDirection subclass
    d = DownDirection()
    s = Spiral(4)
    s.x = 2
    s.y = 1
    #x and y are both within boundaries
    testCheckLocation(d,s,True,"Down")
    #update coordinates to outside boundary
    s.x = 5
    s.y = 1
    testCheckLocation(d,s,False, "Down")
    
    #LeftDirection subclass
    d = LeftDirection()
    s = Spiral(2)
    s.y = 1
    #x and y are both 1 to begin which is valid
    testCheckLocation(d,s,True,"Left")
    #update coordinates to outside boundary
    s.y = -1
    testCheckLocation(d,s,False, "Left")
    
    #UpDirection subclass
    d = UpDirection()
    s = Spiral(3)
    #x and y are both 1 to begin which is valid
    testCheckLocation(d,s,True,"Up")
    #update coordinates to outside boundary
    s.x = -2
    testCheckLocation(d,s,False,"Up")    
    

#Test of subclass function getStartCoordinates
def verifyGetStartCoordinates():
    #check for RightDirection subclass output is correct
    s = Spiral(5)
    d = RightDirection()
    testGetStartCoordinates(s,d,[0,1],"Right")
    s.x = 3
    s.y = 4
    testGetStartCoordinates(s,d,[3,5],"Right")

    #check for DownDirection subclass output is correct
    s = Spiral(5)
    d = DownDirection()
    testGetStartCoordinates(s,d,[1,0],"Down")
    s.x = 1
    s.y = 4
    testGetStartCoordinates(s,d,[2,4],"Down")
    
    #check for LeftDirection subclass output is correct
    s = Spiral(5)
    d = LeftDirection()
    testGetStartCoordinates(s,d,[0,-1],"Left")
    s.x = 3
    s.y = 4
    testGetStartCoordinates(s,d,[3,3],"Left")

    #check for UpDirection subclass output is correct
    s = Spiral(5)
    d = UpDirection()
    testGetStartCoordinates(s,d,[-1,0],"Up")
    s.x = 5
    s.y = 3
    testGetStartCoordinates(s,d,[4,3],"Up")

    
verifyGetNextDirection()
print('\n')
verifyGetDisplacement()
print('\n')
verifyCheckLocation()
print('\n')
verifyGetStartCoordinates()