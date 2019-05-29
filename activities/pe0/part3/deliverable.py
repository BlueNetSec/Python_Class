#!/usr/bin/env python3

def guess_number(n):

    number = int(input("please guess a number between 0 to 100 for fun" + "\n"))
    while(n != number):
        if(number < n):
            print("Too Low")
            number = int(input("please guess a number between 0 to 100 for fun" + "\n"))
        elif(number > n):
            print("Too High")
            number = int(input("please guess a number between 0 to 100 for fun" + "\n"))
        '''else:
           return print("WIN")
           break'''
    print("WIN")   
    return 0

    pass

guess_number(23)
