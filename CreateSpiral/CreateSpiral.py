import sys
from Spiral import Spiral
from Direction import *

#creates the sprial matrix of size N
def createSpiral(N):
    #check that the input is correct, not a string or decimal
    if (not checkInput(N)):
        return
    
    #returns an empty array if n < 1
    if (N < 1):
        print("N = " + str(N) + "   Output: " + str([]))
        return []
    
    #sets base empty array
    array = [[0 for i in range(N)] for j in range(N)]
    #gets instances of sprial and direction objects
    spiral = Spiral(array, N)
    currentDirection = RightDirection()
    
    #fill in spiral until all values are filled
    #uses the function defintion depending on distance object
    #continues in spiral directions (right, down, left, up,...) until done
    #loop breaks when all values are filled in or boundaries are hit
    while (spiral.checkBoundaries() and array[spiral.x][spiral.y] == 0):
        spiral = currentDirection.fillArray(spiral)
        currentDirection.getNextDirection()
        currentDirection = getNextDirectionInstance(currentDirection.currentDirection)
        currentDirection.getStartCoordinates(spiral)
    print("N = " + str(N) + "   Output: " + str(array))
    printPretty(array)
    return array

#gets the next direction object
#the next direction to move in the spiral
def getNextDirectionInstance(n):
    return {
        1 : RightDirection(),
        2 : DownDirection(),
        3 : LeftDirection(),
        0 : UpDirection()
    }[n] 

#prints the matrix pretty
#taken from stackoverflow 10-7-2016
#http://stackoverflow.com/questions/13214809/pretty-print-2d-python-list
def printPretty(matrix):
    print('\n')
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table) )
    print('\n')

#check input values are valid
def checkInput(N):
    if (isinstance(N, int)):
        return True
    else:
        print("N = " + str(N) + " Invalid Input. Enter a positive integer")
        return False

