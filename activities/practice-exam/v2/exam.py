    
#!/usr/bin/env python3

def q1(sentence):
    lis = sentence.split(' ')[::-1]
    return " ".join(lis)
    '''
    Given a string of multiple words separated by single spaces,
    return a new string with the sentence reversed. The words
    themselves should remain as they are. For example, given
    'it is accepted as a masterpiece on strategy', the returned
    string should be 'strategy on masterpiece a as accepted is it'.
    '''
    pass

def q2(n):
    return str(format(n,',d'))
        
    
    '''
    Given a positive integer, return its string representation with
    commas seperating groups of 3 digits. For example, given 65535
    the returned string should be '65,535'.
    '''
    pass

def q3(lst0, lst1):


    return sorted(lst0 + lst1)[::-1]

    '''
    Given two list  s of integers, return a sorted list that contains
    all integers from both lists in descending order. For example,
    given [3,4,9] and [8,1,5] the returned list should be [9,8,5,4,3,1].
    The returned list may contain duplicates.
    '''
    pass

def q4(s1,s2,s3):
    avg = int((s1 + s2 + s3)/3)
    if avg > 50:
        return 'GO'
    else:
        return 'NOGO'
    '''
    Given 3 scores in the range [0-100] inclusive, return 'GO' if
    the average score is greater than 50. Otherwise return 'NOGO'.
    '''
    pass

def q5(integer, limit):
    '''
    a = integer*2
    lis = [0, a]
    mul = 2
    while (a * mul <= limit):
        lis.append(a * mul)
        mul = mul + 1
    return lis
   '''
    '''
    Given an integer and limit, return a list of even multiples of the
    integer up to and including the limit. For example, if integer==3 and
    limit==30, the returned list should be [6,12,18,24,30].
    '''
    pass

def q6(f0, f1):
    #line0 = 0
    #line1 = 0
    '''
    Given two filenames, return a list whose elements consist of line numbers
    for which the two files differ. The first line is considered line 0.
    '''
    pass

def q7(lst):

    '''
    Given a list of integers, return the first value that is duplicated.
    For example, if given [5,7,9,1,3,7,9,5], the returned value should
    be 7.
    '''
    pass

def q8(strng):
    return(len(min(strng.split(' '),key=len)))

    '''
    Given a sentence as a string with words being separated by a single space,
    return the length of the shortest word.
    '''
    pass

def q9(strng):
    '''
    Given an alphanumeric string, return the character whose ascii value
    is that of the integer represenation of all of the digits in the string
    concatenated in the order in which they appear. For example, given
    'hell9oworld7', the returned character should be 'a' which has
    the ascii value of 97.
    '''
    pass

def q10(arr):
    for i in range(len(arr)):
        if arr[i] + 1 != arr[i+1]:
            return (arr[i+1])
        elif i == len(arr):
            return None
            #print(arr[i])
            #print('the end of array')
    '''
    Given a list of positive integers sorted in ascending order, return
    the first non-consecutive value. If all values are consecutive, return
    None. For example, given [1,2,3,4,6,7], the returned value should be 6. 
    '''
    pass

if __name__ == '__main__':
    #q2(1234567)
    #q3([1,3,5],[2,7,8])
    #q5(3,30)
    #q7([5,7,9,1,3,7,9,5])
    #q8('yo AM not HERE who is fucked')
    q10([1,2,3,4,6,7])
