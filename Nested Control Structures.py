'''
Programmer: William Lin
Date: 10/15/19
Program: Double For Loop

This program will nest a For Loop inside of another For Loop
'''

# This program will have both an inner and outer for loop

for i in range(3):
    print ("Outer For Loop: " + str(i))
    for l in range(2):
        print("     Inner For Loop: " +str(l))