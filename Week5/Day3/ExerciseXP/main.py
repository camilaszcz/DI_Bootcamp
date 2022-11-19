# # Exercise 1 : Built-In Functions

# # Instructions
class Abs():
    '''abs() Syntax

# The syntax of abs() method is:

# abs(num)
# abs() Parameters

# abs() method takes a single argument:

# num - a number whose absolute value is to be returned. The number can be:
# integer
# floating number
# complex number

# abs() Return Value

# abs() method returns the absolute value of the given number.

# For integers - integer absolute value is returned
# For floating numbers - floating absolute value is returned
# For complex numbers - magnitude of the number is returned'''

    def do_nothing(self):
        pass
print(Abs.__doc__)



# Example 1: Get absolute value of a number

# # random integer
# integer = -20
# print('Absolute value of -20 is:', abs(integer))

# #random floating number
# floating = -30.33
# print('Absolute value of -30.33 is:', abs(floating))

# Output
# Absolute value of -20 is: 20
# Absolute value of -30.33 is: 30.33
# Example 2: Get magnitude of a complex number

# # random complex number
# complex = (3 - 4j)
# print('Magnitude of 3 - 4j is:', abs(complex))

# Output
# Magnitude of 3 - 4j is: 5.0


class Int():
    '''int() Syntax

The syntax of the int() method is:
int(value, base [optional])
int() Parameters

int() method takes two parameters:

value - any numeric-string, bytes-like object or a number
base [optional] - the number system that the value is currently in

int() Return Value
The int() method returns:

integer portion of the number - for a single argument value (any number)
0 - for no arguments
integer representation of a number with a given base (0, 2 ,8 ,10,16)'''

    def do_nothing(self):
        pass
print(Int.__doc__)

# Example 1: Python int() with a Single Argument

# # int() with an integer value
# print("int(123) is:", int(123))

# # int() with a floating point value
# print("int(123.23) is:", int(123.23))

# # int() with a numeric-string value
# print("int('123') is:", int("123"))


# Output
# int(123) is: 123
# int(123.23) is: 123
# int('123') is: 123
# In the above example, we have returned the integer equivalent of an integer number, a float number and a string value.

# Example 2: int() with Two Arguments

# # converting a binary to integer with int()
# print("For 0b101, int is:", int("0b101", 2))

# # converting a binary to integer with int())
# print("For 0o16, int is:", int("0o16", 8))

# # converting a binary to integer with int()
# print("For 0xA, int is:", int("0xA", 16))

# Output
# For 0b101, int is: 5
# For 0o16, int is: 14
# For 0xA, int is: 10

# Example 3: int() for custom objects

# Even if an object isn't a number, we can still convert it to an integer object.
# We can do this easily by overriding __index__() and __int__() methods of the class to return a number.
# The two methods are identical. The newer version of Python uses the __index__() method.

# class Person:
#     age = 23

#     def __index__(self):
#         return self.age

#     # def __int__(self):
#     #     return self.age

# person = Person()

# # int() method with a non integer object person
# print("int(person) is:", int(person))

# Output
# int(person) is: 23
# In the above example, the class Person is not of the integer type.

# But we can still return the age variable (which is an integer) using the int() method.



class Input():

    '''# input() Syntax

# The syntax of input() function is:

# input([prompt])
# input() Parameters

# The input() function takes a single optional argument:

# prompt (Optional) - a string that is written to standard output (usually screen) without trailing newline
# input() Return Value

# The input() function reads a line from the input (usually from the user), converts the line into a string by removing the trailing newline, and returns it.

# If EOF is read, it raises an EOFError exception.'''

# Example 1: How input() works in Python?

# # get input from user

# inputString = input()

# print('The inputted string is:', inputString)
# Output

# Python is interesting.
# The inputted string is: Python is interesting
# Example 2: Get input from user with a prompt

# # get input from user

# inputString = input('Enter a string:')

# print('The inputted string is:', inputString)

# Output
# Enter a string: Python is interesting.
# The inputted string is: Python is interesting

# Using the __doc__ dunder method create your own documentation which explains the execution of your code:
class Doc:
    
    def do_nothing(self):
        pass
print(Input.__doc__)

# Exercise 2: Currencies

# Instructions

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        
    def __add__(self, amount, other):
        
        if type(other)==int:
            return Currency(self.amount + other)
        else:
            return Currency(self.amount + other.amount)
        
    def __str__(self):
       return f'{self.amount} {self.currency}s'
   
    def __repr__(self):
        return f'Currency(amount={self.amount}, currency={self.currency})'
    
    def __int__(self):
        return int(self.amount)
        
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1.__str__())
# >>> str(c1)
# '5 dollars'

print(c1.__int__())
# >>> int(c1)
# 5

print(c1.__repr__())
# >>> repr(c1)
# '5 dollars' . /// would be the same as str
# Currency(amount=5, currency=dollar)

# print(c1.__add__(5))
print(c1.amount + 5)
# # 10

# print(c1.amount + c2.amount)
# print(c1.__add__(c2))
# print(c1+c2)
# 15

print(c1.__str__())
# c1 
# 5 dollars

print(c1.amount + 5)
# >>> c1 += 5
# >>> c1
# 10 dollars


print(c1.amount + c2.amount)
# >>> c1 += c2
# >>> c1
# 20 dollars

# print(c1.__add__(c3))
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>


# // Missed something on the sintax, keep getting an error of a missing argument. 
# All examples have only one parameter. Since this one has two, I don't know how to call specifically the second on the add metthod