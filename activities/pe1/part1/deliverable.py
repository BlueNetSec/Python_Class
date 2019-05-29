#!/usr/bin/env python3

def invert(l):
    index = 0
    for element in l:
        l[index] = str(255 - int(element))
        index = index + 1
    return  
       
    '''Inverts the given list
    Args:
        l (list): list of strings representing integers in the range [0-255]
    Returns:
        None
    '''
    pass

def inverted(l):
    index = 0
    newlist = l[:]
    for element in newlist:
        newlist[index] = str(255 - int(element))
        index = index + 1
    return newlist
    '''Returns a new list that is the given list inverted
    Args:
        l (list): list of strings representing integers in the range [0-255]
    Returns:
        list: new list that is the given list inverted
    '''
    pass

if __name__ == '__main__':
    #a = [1,2,3,4,5]
    #print(inverted(a))    
    pass
