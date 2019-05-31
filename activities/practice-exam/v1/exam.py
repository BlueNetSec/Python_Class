#!/usr/bin/env python3

def q1(floatstr):
    '''
    TLO: 112-SCRPY002, LSA 3,4
    Given the floatstr, which is a comma separated string of
    floats, return a list with each of the floats in the 
    argument as elements in the list.
      '''
 
    lis = []    
    a = floatstr.split(',')
    for char in a:
        char = float(char)
        lis.append(char)
    return lis
    
    pass

def q2(*args):
    summ = 0.0
    counter = 0
    for arg in args:
        summ = summ + float(arg)
        counter = counter + 1
    return float(summ/counter)
    '''
    TLO: 112-SCRPY006, LSA 3
    TLO: 112-SCRPY007, LSA 4
    Given the variable length argument list, return the average
    of all the arguments as a float
    '''
    pass

def q3(lst,n):
    
    '''
    TLO: 112-SCRPY004, LSA 3
    Given a list (lst) and a number of items (n), return a new 
    list containing the last n entries in lst.
    '''
    lit2 = lst[::-1]
    lit3 = lit2[:n]
    return lit3[::-1]
    #index = int(-1 * n)
    #return lst(index:-1)
       
    pass
    
def q4(strng):
    '''
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY006, LSA 3
    Given an input string, return a list containing the ordinal numbers of 
    each character in the string in the order found in the input string.
    '''
    num = []
    #lis = strng.split()
    for a in strng:
        num.append(ord(a))
    return num
    pass

def q5(strng):
    return tuple(strng.split())
    '''
    TLO: 112-SCRPY002, LSA 1,3
    TLO: 112-SCRPY004, LSA 2
    Given an input string, return a tuple with each element in the tuple
    containing a single word from the input string in order.
    '''
    pass

def q6():
    
    return 'Im the Boss'
    '''
    TLO: 112-SCRPY006, LSA 4
    Given an input string similar to the below, craft a regular expression  
    pattern to match and extract the date, time, and temperature in groups  
    and return this pattern. Samples given below.
    Date: 12/31/1999 Time: 11:59 p.m. Temperature: 44 F
    Date: 01/01/2000 Time: 12:01 a.m. Temperature: 5.2 C
    '''
    pass

def q7(filename):
    f = open(filename)
    data = f.readline()
    return len(data)-1
    '''
    TLO: 112-SCRPY005, LSA 1
    Given a filename, open the file and return the length of the first line 
    in the file excluding the line terminator.
    '''
    pass

def q8(filename,lst):
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY005, LSA 1
    Given a filename and a list, write each entry from the list to the file
    on separate lines until a case-insensitive entry of "stop" is found in 
    the list. If "stop" is not found in the list, write the entire list to 
    the file on separate lines.
    '''
    with open(filename,'a') as f:
        for a in lst:
            if a.lower() != 'stop':
                f.write(a)
                f.write('\n')
            else:
                break   
    pass

def q9(miltime):
    message = ''
    if  1200 <= int(miltime) <= 1559:
        message = "Good Afternoon"
    elif 1600 <= int(miltime) <= 2059:
        message = "Good Evening"
    elif 300 <= int(miltime) <= 1159:
        message = "Good Morning"
    else:
        message = "Good Night"
    return message
    '''
    TLO: 112-SCRPY003, LSA 1
    Given the military time in the argument miltime, return a string 
    containing the greeting of the day.
    0300-1159 "Good Morning"
    1200-1559 "Good Afternoon"
    1600-2059 "Good Evening"
    2100-0259 "Good Night"
    '''
    pass
    
def q10(numlist):

    for a in numlist:
        if a < 0:
            return False
        else:
            return True
            
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1
    Given the argument numlist as a list of numbers, return True if all 
    numbers in the list are NOT negative. If any numbers in the list are
    negative, return False.
    '''
    pass
#if __name__ == '__main__':

    #a = q1('2.5,2.6,5.7')
