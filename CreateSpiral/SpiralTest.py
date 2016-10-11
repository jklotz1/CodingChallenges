from Spiral import *
from Direction import *

#verify that the function output matches the expected output
def verifyFunctionOutput(functionOutput, expectedOutput):
    return (functionOutput == expectedOutput)


def testCheckBoundaries(s, expected):
    print("when x = " + str(s.x) + "   y = " + str(s.y) + " and n = " 
          + str(s.n) + " and array = " + str(s.array))
    print('checkBoundaries() == ' + str(expected))
    print("Result: " + str(verifyFunctionOutput(s.checkBoundaries(), 
                                                expected)))  

def testGetNextDirectionInstance(s, expected, direction):
    print("type(getNextDirectionInstance(" 
          + str(s.direction.currentDirection) + ")) == type(" + direction
          + "Direction())")
    print("Result: " 
          + str(verifyFunctionOutput(type(s.getNextDirectionInstance())
                                                , type(expected))))    

def testGetNextDirection(s, expected, exType, old, new):
    print("when currentDirection = " + str(s.direction.currentDirection) 
          + " and type = " + old + "Direction")
    print('getNextDirection() results in currentDirection == ' 
          + str(expected) + " and type == " + new + "Direction")
    s.getNextDirection()
    print("Result: " + str(verifyFunctionOutput(s.direction.currentDirection, 
                                                expected) and
                           verifyFunctionOutput(type(s.direction), 
                                                type(exType))))     
    

def testCreateSpiral(s, expected):
    print('when N = ' + str(s.n) + ' fillArray() == ' + str(expected))
    print("Result: " + str(verifyFunctionOutput(s.fillArray().array, 
                                                expected)))  

def verifyCheckBoundaries():
    #create a spiral instance
    #case when array[x,y] == 0 and x and y are within the location boundaries 
    s = Spiral(2)
    s.array = [[0,0],[2,1]]
    #initailly x = 0 and y = 0
    #checkBoundaries evaluates to True and not False
    testCheckBoundaries(s, True)

    s.x = 3
    s.y = 3
    #update x and y values
    #x and y are now beyond the boundary(0 to n)
    #checkBoundaries evaluates to False
    testCheckBoundaries(s, False)

    #update x and y are within the boundary but array[x][y] != 0
    #checkBoundaries evaluates to False
    s.x = 1
    s.y = 1
    testCheckBoundaries(s, False)
    
    #x and y with in the boundary and array[x][y] != 0
    #direction is changed
    #checkBoundaries will evaluate to True
    s.direction = LeftDirection()
    s.x = 0
    s.y = 1
    testCheckBoundaries(s, True)
    
    #x and y are beyond the boundary
    #checkBoundaries evaluates to False
    s.x = 0 
    s.y = -1
    testCheckBoundaries(s, False)
   

def verifyGetNextDirectionInstance():
    #verify getNextDirectionInstance function
    #compare type of function output to type of expected output
    #start with a spiral object, initalized to RightDirection
    #then change the currentDirection value and make sure right type
    s = Spiral(5)
    testGetNextDirectionInstance(s, RightDirection(), "Right")
    s.direction.currentDirection = 2
    testGetNextDirectionInstance(s, DownDirection(), "Down")
    s.direction.currentDirection = 3
    testGetNextDirectionInstance(s, LeftDirection(), "Left")
    s.direction.currentDirection = 0
    testGetNextDirectionInstance(s, UpDirection(), "Up")  
  

def verifyGetNextDirection():
    #create spiral object
    #intial currentDirection = 1
    s = Spiral(2)
    #verify that the next direction is the one that is expected
    testGetNextDirection(s, 2, DownDirection(), "Right", "Down")
    testGetNextDirection(s, 3, LeftDirection(), "Down", "Left") 
    testGetNextDirection(s, 0, UpDirection(), "Left", "Up") 
    testGetNextDirection(s, 1, RightDirection(), "Up", "Right")
    
def verifyFillArray():
    s = Spiral(1)
    testCreateSpiral(s, [[1]])
    s = Spiral(2)
    testCreateSpiral(s, [[1,2],[4,3]])
    s = Spiral(4)
    testCreateSpiral(s, [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]])
   
      
    
verifyCheckBoundaries()
print('\n')
verifyGetNextDirectionInstance()
print('\n')
verifyGetNextDirection()
print('\n')
verifyFillArray()
