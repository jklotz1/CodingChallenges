from NextVersion import nextVersion

#verify that the function output matches the expected output
def verifyFunctionOutput(functionOutput, expectedOutput):
    return (functionOutput == expectedOutput)

#verify that the function doesn't match the given output
def verifyFunctionOutputIncorrect(functionOutput, output):
    return (functionOutput != output)

def testNextVersion(input, output):
    print('nextVersion("' + input + '") == "' + output + '"')
    print("Result: " + str(verifyFunctionOutput(nextVersion(input), output)))

def testNextVersionIncorrect(input, output):
    print('nextVersion("' + input + '") != ' + str(output))
    print("Result: " + str(verifyFunctionOutputIncorrect(nextVersion(input), 
                                                        output)))


#verify that the number increases  
testNextVersion("0","1")

#verify that the function output is a string
#check against an int - the output shouldn't be an int
testNextVersionIncorrect("0",1)

#verify that the version is incremented
#only the last number will be affected
testNextVersion("0.1","0.2")
testNextVersion("0.0.1","0.0.2")
testNextVersion("1.1.1","1.1.2")
testNextVersion("1.2.3","1.2.4")

#verify incrementing 9 by 1 will increment the next number in the sequence
testNextVersion("0.9.9","1.0.0")

#verify that incrementing 9 in the first position results in 10
testNextVersion("9.9.9","10.0.0")

#verify that incrementing the version affects the correct numbers
testNextVersion("9.0.9","9.1.0")
testNextVersion("1.0.9.9","1.1.0.0")
testNextVersion("1.2.3.4.5.6.7.8","1.2.3.4.5.6.7.9")

