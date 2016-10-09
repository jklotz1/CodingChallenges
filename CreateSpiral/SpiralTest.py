from Spiral import *

#verify that the function output matches the expected output
def verifyFunctionOutput(functionOutput, expectedOutput):
    return (functionOutput == expectedOutput)

#verify that the function doesn't match the given output
def verifyFunctionOutputIncorrect(functionOutput, output):
    return (functionOutput != output)


def testCheckBoundaries(s, expected):
    print('checkBoundaries() == ' + str(expected))
    print("when x = " + str(s.x) + "   y = " + str(s.y) + " and n = " 
          + str(s.n))
    print("Result: " + str(verifyFunctionOutput(s.checkBoundaries(), 
                                                expected)))
    
def testCheckBoundariesIncorrect(s, expected):
    print('checkBoundaries() != ' + str(expected))
    print("when x = " + str(s.x) + "   y = " + str(s.y) + " and n = " 
          + str(s.n))
    print("Result: " + str(verifyFunctionOutputIncorrect(s.checkBoundaries(),
                                                         expected)))    


def verifyCheckBoundaries():
    #create a spiral instance
    s = Spiral([], 5)
    #initailly x = 0 and y = 0
    #checkBoundaries evaluates to True and not False
    testCheckBoundaries(s, True)
    testCheckBoundariesIncorrect(s, False)

    s.x = 3
    s.y = 3
    
    #update x and y values
    #checkBoundaries evaluates to True
    testCheckBoundaries(s, True)

    #update x and y values to greater than the boundary (n)
    #checkBoundaries evaluates to False and not True      
    s.x = 5
    testCheckBoundaries(s, False)
    testCheckBoundariesIncorrect(s, True)

    s.y = 5
    testCheckBoundaries(s, False)

    s.x = 10
    testCheckBoundaries(s, False)
    testCheckBoundariesIncorrect(s, True)
    
verifyCheckBoundaries()