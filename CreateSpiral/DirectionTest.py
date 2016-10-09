from Direction import *
from Spiral import *

#verify that the function output matches the expected output
def verifyFunctionOutput(functionOutput, expectedOutput):
    return (functionOutput == expectedOutput)

def testGetNextDirection(d, expected):
    print("when currentDirection = " + str(d.currentDirection))
    print('getNextDirection() results in currentDirection == ' 
          + str(expected))
    d.getNextDirection()
    print("Result: " + str(verifyFunctionOutput(d.currentDirection, 
                                                expected))) 

def testFillArray(d, s, expected, direction):
    print("when array = " + str(s.array) + " and value = " + str(s.value))
    print('fillArray() for ' + direction + 'Direction results in ' 
          + str(expected))
    d.fillArray(s)
    print("Result: " + str(verifyFunctionOutput(s.array, expected)))
    
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
    testGetNextDirection(d, 1)
    testGetNextDirection(d, 2)
    
    #verify with subclass
    #RightDirection sets currentDirection = 1
    d = RightDirection()
    testGetNextDirection(d, 2)
    testGetNextDirection(d, 3)      
    
#test functions of the subclasses

def verifyFillArray():
    #try for RightDirection
    d = RightDirection()  
    #fills the correct direction
    s = Spiral([[0,0,0],[]], 3)
    testFillArray(d,s,[[1,2,3],[]],"Right")
    
    
    #fills until it hits a value
    s = Spiral([[],['x',0,0,'x']], 4)
    s.x = 1
    s.y = 1
    testFillArray(d,s,[[],['x',1,2,'x']],"Right")

    #test for LeftDirection
    d = LeftDirection()    
    #fills correct direction
    s = Spiral([[0,0,0],[]], 3)
    s.y = 2
    testFillArray(d,s,[[3,2,1],[]],"Left")

    #fills with the value given in spiral until it hits a value
    s = Spiral([[],['x',0,0,'x']], 4)
    s.x = 1
    s.y = 2
    s.value = 5
    testFillArray(d,s,[[],['x',6,5,'x']],"Left")

    #test for UpDirection
    d = UpDirection() 
    #fills the correct direction
    s = Spiral([[0,0],[0,0]], 2)
    s.x = 1
    s.y = 1
    testFillArray(d,s,[[0,2],[0,1]],"Up")

    #fills until it hits a value
    s = Spiral([[0,'x',0],[0,0,0],[0,0,0]], 3)
    s.x = 2
    s.y = 1
    s.value = 10
    testFillArray(d,s,[[0,'x',0],[0,11,0],[0,10,0]],"Up")

    #test for DownDirection
    d = DownDirection()    
    s = Spiral([[0,0],[0,0]], 2)
    testFillArray(d,s,[[1,0],[2,0]],"Down")

    s = Spiral([[0,0,0],[0,0,0],[0,'x',0]], 3)
    s.x = 0
    s.y = 1
    s.value = 7
    testFillArray(d,s,[[0,7,0],[0,8,0],[0,'x',0]],"Down")


#Test of subclass function getStartCoordinates
def verifyGetStartCoordinates():
    #check for RightDirection subclass output is correct
    s = Spiral([], 5)
    d = RightDirection()
    testGetStartCoordinates(s,d,[0,1],"Right")
    
    s.x = 3
    s.y = 4
    testGetStartCoordinates(s,d,[3,5],"Right")

    #check for DownDirection subclass output is correct
    s = Spiral([], 5)
    d = DownDirection()
    testGetStartCoordinates(s,d,[1,0],"Down")
   
    s.x = 1
    s.y = 4
    testGetStartCoordinates(s,d,[2,4],"Down")
    
    #check for LeftDirection subclass output is correct
    s = Spiral([], 5)
    d = LeftDirection()
    testGetStartCoordinates(s,d,[0,-1],"Left")

    s.x = 3
    s.y = 4
    testGetStartCoordinates(s,d,[3,3],"Left")

    #check for UpDirection subclass output is correct
    s = Spiral([], 5)
    d = UpDirection()
    testGetStartCoordinates(s,d,[-1,0],"Up")

    s.x = 5
    s.y = 3
    testGetStartCoordinates(s,d,[4,3],"Up")

    
verifyGetNextDirection()
print('\n')
verifyFillArray()
print('\n')
verifyGetStartCoordinates()