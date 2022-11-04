# Exercise 1 : What Are You Learning ?


# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.


#  Exercise 2: What’s Your Favorite Book ?


# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.


# Exercise 3 : Some Geography

# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>". 
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.


# Exercise 4 : Random


# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.


# Exercise 5 : Let’s Create Some Personalized Shirts !


# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message. 

# Bonus: Call the function make_shirt() using keyword arguments.


#  Exercise 6 : Magicians …

# Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.


#Exercise 7 : Temperature Advice

import random

SEASONS={
    'winter': (-10,16),
    'summer': (28,40),
    'autumn': (15,24),
    'fall': (10,24)
}
def get_random_temp(season:str):
    temp_range = SEASONS.get(season)
    if temp_range:
        
        temperature = random.randint(*temp_range)
        return temperature
    else:
        return 0

temp= SEASONS.get('summer')
print(temp)

def main():
    
    user_in = input("TEMPERATURE FOR WINTER/FALL/SUMMER/SPRING:")
    rand_temp = get_random_temp
    print(f'The temperature right now is {rand_temp} degrees Celsius.')
    if rand_temp<0:
        print('brrr')
    elif 0<= rand_temp <16:
        print ('chilly')
    elif 16<= rand_temp <23:
        print('between')
    else:
        print('between 32 and 40')    
        
    print(f'the temperature righ now is {rand_temp} degrees Celsius')

main()  
