# Exercise 1 : Convert Lists Into Dictionaries

# Convert the two following lists, into dictionaries.
# Zip the lists together using zip(list_1, list_2).
# Create a dictionary from the list of tuples using the constructor dict() on the result.
# In other words, call dict(zip(list_1, list_2)) to convert two lists into a dictionary.

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]


# dictionary = dict(zip(keys, values))
# print(dictionary)


# Exercise 2 : Cinema 
# //////Got completely stuck! something happened in the middle and I couldnt come back from it!/////

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Bonus: Ask the user to input the names and ages instead of using the provided family variable 
# (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

# cinema = {}

# for i in range(4):
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")

# cinema[name]=age

# print(cinema)

# How much does each family member have to pay ?

# price_list = cinema.values()

# if cinema[age] < 3:
#         print("Your ticket is free")
# elif cinema[age] < 12:
#         print("Your ticket is $10") 
# else:
#         print("Your ticket is $15")
# print(cinema)

# total_cost = sum()

# Print out the family’s total cost for the movies.

# Exercise 3: Zara
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
brand= {
'name': 'Zara',
'creation_date': 1975, 
'creator_name': 'Amancio' 'Ortega' 'Gaona' ,
'type_of_clothes': ['men', 'women', 'children', 'home'],
'international_competitors': ['Gap', 'HM', 'Benetton' ],
'number_stores': 7000 ,
'major_color': {
    'France': 'blue', 
    'Spain': 'red', 
    'US': ['pink', 'green']},
}

# 3. Change the number of stores to 2.
brand['number_stores']= 2

# 4. Print a sentence that explains who Zaras clients are.
print(','.join(brand['type_of_clothes']))
# 5. Add a key called country_creation with a value of Spain.
brand['country_creation'] = 'Spain',
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
# 7. Delete the information about the date of creation.
del brand['creation_date']
# 8. Print the last international competitor.
print((brand['international_competitors'][-1]))
# 9. Print the major clothes colors in the US. 
print(brand['major_color']['US'])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))
# 11. Print the keys of the dictionary.
print(brand.keys())
# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
more_on_zara={
    'creation_date':1975,
    'number_stores':10000,
    }
brand.update(more_on_zara)
# 14. Print the value of the key number_stores. What just happened ?

print(brand['number_stores'])
#Result 10000


# Exercise 4 : Disney Characters//Will come back to it

# Use this list :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.
