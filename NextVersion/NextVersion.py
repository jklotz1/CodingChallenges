import sys

#given a version, nextVersion will return the next version number
def nextVersion(oldVersion):
    #the given version is converted to an array without the '.'
    old = oldVersion.split('.')
    carry = 1
    
    #iterate through array from end to begining, increment by one
    #use carry if a value needs to carry over to other numbers
    for i in range(len(old)-1, -1, -1):
        if (i  == 0):
            value = str((int(old[i]) + carry))
        else:
            value = str((int(old[i]) + carry) % 10)
            carry = (int(old[i]) + carry) // 10
            
        old[i] = value

    #convert the array back to string with '.' delimiter
    next = ".".join(old)
    print("The version entered: " + oldVersion)
    print("The next version: " + next + '\n')
    
    #return the next version
    return next

 