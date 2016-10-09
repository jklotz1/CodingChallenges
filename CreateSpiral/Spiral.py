#class definition of Spiral class
#  current x,y position when filling in the spiral
#  array that gets filled in
#  the next value that will fill the spiral in
#  n is the boundary
class Spiral():
    x = 0 
    y = 0
    array = []
    value = 1
    n = 0
    
    def __init__(self, _array, _n):
        self.array = _array
        self.n = _n
        
    #checks to see if the x or y values exceeds the boundary n
    #used as a breaking condition
    def checkBoundaries(self):
        return (self.x < self.n and self.y < self.n)