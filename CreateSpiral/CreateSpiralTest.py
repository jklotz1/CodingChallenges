from CreateSpiral import *
from Direction import *

#verify that the function output matches the expected output
def verifyFunctionOutput(functionOutput, expectedOutput):
    return (functionOutput == expectedOutput)

def testCreateSpiral(input, expected):
    print('createSpiral(' + str(input) + ') == ' + str(expected))
    print("Result: " + str(verifyFunctionOutput(createSpiral(input), 
                                                expected)))   
def testCheckInput(input, expected):
    print('checkInput(' + str(input) + ') == ' + str(expected))
    print("Result: " + str(verifyFunctionOutput(checkInput(input), expected))) 

def testGetNextDirectionInstance(input, expected, direction):
    print("type(getNextDirectionInstance(" + str(input) + 
          ")) == type(" + direction + "Direction())")
    print("Result: " 
          + str(verifyFunctionOutput(type(getNextDirectionInstance(input))
                                                , type(expected))))    
    
#verify createSpiral function
#when N is less than 1 then empty array is returned
testCreateSpiral(0,[])
testCreateSpiral(-2, [])
testCreateSpiral(1, [[1]])
testCreateSpiral(3, [[1,2,3],[8,9,4],[7,6,5]])
testCreateSpiral(6, [[1,2,3,4,5,6],[20,21,22,23,24,7],[19,32,33,34,25,8],
                         [18,31,36,35,26,9],[17,30,29,28,27,10], 
                         [16,15,14,13,12,11]])
print('\n')

#verifications of additional methods in CreateSpiral.py

#integers are accepted
testCheckInput(1, True)

#negative integers are accepted
testCheckInput(-1, True)

#strings are not accepted
testCheckInput('abc', False)

#empty string is not accpeted
testCheckInput('',False)

#none integer numbers are not accepted
testCheckInput(1.2, False)

print('\n')

#verify getNextDirectionInstance function
#compare type of function output to type of expected output
testGetNextDirectionInstance(1,RightDirection(),"Right")
testGetNextDirectionInstance(2,DownDirection(),"Down")
testGetNextDirectionInstance(3,LeftDirection(),"Left")
testGetNextDirectionInstance(0,UpDirection(),"Up")