import sys
from Spiral import *
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
    
    #get instances of the spiral 
    spiral = Spiral(N) 
    #fill the array with numbers
    spiral.fillArray()

    print("N = " + str(N) + "   Output: " + str(spiral.array))
    printPretty(spiral.array)
    return spiral.array

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

