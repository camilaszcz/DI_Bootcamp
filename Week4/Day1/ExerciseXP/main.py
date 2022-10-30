# Week4Day1
# ExercisesXP


from distutils.log import info


print (5 *'Hello world\n')

# >>> print (5 *'Hello world\n')
# Hello world
# Hello world
# Hello world
# Hello world
# Hello world


# Exercise2
# Write code that calculates the result of: (99^3) * 8 (99 to the power of 3 times 8)

99**3*8
# result:7762392

# Exercise3
# False
# True
# False
# Error?
# False

# Exercise4
computer_brand = 'Apple'
print = ('I have a'+ computer_brand +'computer')

# Result: 'I have aApplecomputer'

#Exercise5

name = 'Camila'
age = 33
shoe_size = 38
info = ('My name is'+ name + 'and people think that I am younger than' + str(age) + 'and my feet are bigger than' + str(shoe_size))
   
print (info)

#Exercise6
a=9
b=8
if a>b:
    print ('Hello World')
    
#Exercise7
#Write code that asks the user for a number and determines whether this number is odd or even

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
    
#Exercise8
#Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

name = input("Enter your name: ")
if name == 'Camila':
    print("Oh no!Double trouble")
else:
    print('What a nice name!')
    



