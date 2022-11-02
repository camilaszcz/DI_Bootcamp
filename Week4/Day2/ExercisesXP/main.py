
# Exercise 1 : Set

# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {8,7,47,24}
my_fav_numbers.add(55)
my_fav_numbers.add(13)

print(my_fav_numbers)

my_fav_numbers.remove(13)

friend_fav_numbers= {18,32,45}

our_fav_numbers=  my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


#Exercise 2: Tuple
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
a_tuple = (1,2,3,4)

#Answer:No, tuples are not mutable


#Exercise 3: List

# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove “Banana” from the list.
basket.remove('Banana')
# Remove “Blueberries” from the list.
basket.remove('Blueberries')
# Add “Kiwi” to the end of the list.
basket.append('Kiwi')
# Add “Apples” to the beginning of the list.
basket.insert(0,'Apples')
print(basket)

# Count how many apples are in the basket.
print(basket.count('Apples'))

# Empty the basket.
# basket.remove(::)   #???
# Print(basket)
print(basket)


# Exercise 4: Floats

# Recap – What is a float? What is the difference between an integer and a float?
    #Answer: An integer in a full number and a float is a number with decimals after a dot. 

# Can you think of another way to generate a sequence of floats?
from asyncio.base_futures import _FINISHED
import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

print(list(float_range(0, 1, '0.1')))

# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

print(list(float_range(0, 1, '0.5')))

# Exercise 5: For Loop
# for iter in sequence:
#     statements(iter)
    
    
# Use a for loop to print all numbers from 1 to 20, inclusive.

for iter in range(1,21):
    print(iter)

# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
for iter in range(1,21):
    if iter %2 == 0:
        print(iter)

# Exercise 6 : While Loop
# Write a while loop that will continuously ask the user for their name, 
# unless the input is equal to your name.
myName = ('Camila')


while True:
    answer = input('Whats your name')
    if answer == myName:
        break
    
#Exercise 7: Favorite Fruits

# Ask the user to input their favorite fruit(s) (one or several fruits). 

fruits = input ('Your favorite fruits:').split('')
print('Fruits chosen:' , fruits)

user_fruit = input ('Choose a fruit:')

if user_fruit in fruits:
    print('You chose one of your favorite fruits!Enjoy')
else: 
      print('You chose a new fruit. I hope you enjoy')

# Exercise 8: Who Ordered A Pizza ?

# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
toppings = []

user_in = ''

while user_in!= 'Quit':
    topping= input ('Add a new topping:')
    toppings.append(topping)
    
# # print(f'You've added {topping} to your pizza')
#       toppings.append(topping)
      
#       ///couldnt _FINISH
      
# Exercise 9: Cinemax

# Instructions

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.


# Exercise 10 : Sandwich Orders

# Instructions

# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.


# Exercise 11 : Sandwich Orders#2

# Instructions

# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.