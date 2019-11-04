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

print("\n-------------------------------------------\n")
'''
Programmer: William Lin
Date: 10/22/19

Program: Average Test Score

This program asks for the test scores of multiple people and reports the average test score for each portion
'''

num_people = int(input("How many people took the test?: "))
test_score = int(input("How many tests are going to be averaged?: "))
for i in range(num_people):
name = input("Enter name: ")
sum = 0
for j in range(test_score):
    score = int(input("  Enter a score: "))
    sum = sum + score
average = float(sum/test_score)
print (name + " got an average of " + str(round)(average, 2))

print("\n-------------------------------------------\n")
'''
Programmer: William Lin
Date: 10.22.19
Program: For Loop + While Loop

This program will incorporate a For Loop embedding a While Loop in it
'''
for i in range(4):
    print("Outer For Loop: " + str(i))
    x = 1
    while x>= 6:
        print("    While Loop: " + str(x))
        x = x - 1
    

