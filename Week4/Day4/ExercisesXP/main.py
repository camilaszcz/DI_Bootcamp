# Exercise 1 : What Are You Learning ?

# def display_message():
#     print("I am learning Python!") 

# display_message()

#  Exercise 2: What’s Your Favorite Book ?

# def favorite_book(title):
#     print('One of my favorite books is' + title)

# favorite_book(' 1984')  


# Exercise 3 : Some Geography

# def describe_city(city, country='Brasil'):

#     display = city.title() + " is in " + country.title() + "."
#     print(display)

# describe_city('Rio de Janeiro')


# Exercise 4 : Random///// 


# import random

# def guess():
#     number = random.randint(1, 100)
#     user_input = -1
#     num_guesses = 0
#     while True:
#         user_input = int(input("Guess the number I am thinking of: "))
#         if user_input == number:
#             print ('Success')
#             break  # we got the correct answer, so end.
#         elif user_input <= 0 or user_input > 100:
#             print ("I thought I said something between 0 and 100!")
#             continue 
#         elif user_input < number:
#             print ("Too low!")
#         elif user_input > number:
#             print ("Too high!")
#         num_guesses = num_guesses+1

#     print ("You're right! You took", num_guesses, "wrong guesses before you got the answer")

# guess()


# Exercise 5 : Let’s Create Some Personalized Shirts !


# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# def make_shirt(size, message):

#     print("\nI'm going to make a " + size + " t-shirt.")
#     print('It will say, "' + message + '"')

# make_shirt('medium', 'I love Python!')
# make_shirt(message="Study harder!", size='medium')


# # Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# # Make a large shirt with the default message
# # Make medium shirt with the default message
# # Make a shirt of any size with a different message. 

# def make_shirt(size='large', message='I love Python!'):
#     print("\nI'm going to make a " + size + " t-shirt.")
#     print('It will say, "' + message + '"')

# make_shirt()
# make_shirt(size='medium')
# make_shirt('small', 'This thing is not easy.')

# Bonus: Call the function make_shirt() using keyword arguments. // 


#  Exercise 6 : Magicians

# Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.

# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician.title())

# magicians = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# show_magicians(magicians)

# # Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# # Call the function make_great().
# # Call the function show_magicians() to see that the list has actually been modified.
# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)

# def make_great(magicians):
#     great_magicians = []

#     while magicians:
#         magician = magicians.pop()
#         great_magician = magician + ' the Great'
#         great_magicians.append(great_magician)

#     for great_magician in great_magicians:
#         magicians.append(great_magician)

# magicians = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# show_magicians(magicians)

# print("\n")
# make_great(magicians)
# show_magicians(magicians)

#Exercise 7 : Temperature Advice

# import random

# SEASONS = {
#     'winter': (-10, 16),
#     'summer': (28, 40),
#     'autumn': (15, 24),
#     'fall': (10, 24),
# } 

# def get_random_temp(season: str):
#     # .get returns Value or None
#     temp_range = SEASONS.get('season')
#     if temp_range:

#         temperature = random.randint(*temp_range)
#         return temperature
   
#     return 0


# def main():
    
#     user_in = input("Temperature for winter/fall/spring/summer: ")

#     rand_temp = get_random_temp(season=user_in)

#     if rand_temp < 0:
#         print('Brrr, thats freezing! Wear some extra layers today')
#     elif 0 <= rand_temp < 16:
#         print("Quite chilly! Don't forget your coat")
#     elif 16 <= rand_temp < 23:
#         print('between 16 and 23')
#     elif 16 <= rand_temp < 32:
#         print('between 24 and 32')
#     else:
#         print('between 32 and 40')  

#     print(f"The temperature right now is {rand_temp} degrees Celsius.")


# main()
