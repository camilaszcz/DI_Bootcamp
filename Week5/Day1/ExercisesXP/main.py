# 🌟 Exercise 1: Cats

# from functools import reduce

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# cat1 = Cat("Cherrie", 8)
# cat2 = Cat("Hamud", 4)
# cat3 = Cat("Agata", 6)

# cats = [cat1,cat2,cat3]

# oldest_cat_func = lambda cat1, cat2: cat1 if cat1.age > cat2.age else cat2
# oldest_cat = reduce(oldest_cat_func, cats)

# # print(oldest_cat.name)


# print(f'The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.')


# # 🌟 Exercise 2 : Dogs

# # Instructions

# # Create a class called Dog.
# # In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters
        
# # class Dog():
# #     def __init__(self, name, height):
# #         self.name = name
# #         self.height = height
        

# # Create a method called bark that prints the following string “<dog_name> goes woof!”.
# # using and accessing global class attributes

    
# class Dog():
#     bark = 'goes woof!'  # global attribute, accessible through the class itself

#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
        
        
# print((Dog('Sam', 50)).name, Dog.bark)


# # Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.

# # Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# # Print the details of his dog (ie. name and height) and call the methods bark and jump.
# # Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# # Print the details of her dog (ie. name and height) and call the methods bark and jump.
# # Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
# class Dog:

#     def __init__(self, name: str, height: int):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         x = self.height * 2
#         print(f"{self.name} jumps {x} cm high!")

#     def __str__(self):
#         return f"{self.name}, {self.height}"
        
# davids_dog = Dog('Rex', 50)

# print(davids_dog)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog('Teacup', 20)
# print(sarahs_dog)
# sarahs_dog.bark()
# sarahs_dog.jump()

# bigger_dog = sarahs_dog.name if sarahs_dog.height > davids_dog.height else davids_dog.name

# print(bigger_dog)

# Exercise 3 : Who’s The Song Producer?

# Instructions

# Define a class called Song, it will show the lyrics of a song.

# class Song(object):
#     def __init__(self, lyrics):
#         self.lyrics=lyrics
    
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print (line)

# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# print (stairway.sing_me_a_song())


# Exercise 4 : Afternoon At The Zoo

# Instructions









# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).

class Zoo():
      
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animal  =[]
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
    def add_animal(new_animal):
        if new_animal != 0:
            new_animal.append(animals_list)
        else:
            pass
# Create a method called get_animals that prints all the animals of the zoo.
    def get_animal(self):
        return self.animals_list      
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
    def sell_animal(animal_sold):
        return self.animals_list-1
            
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter. 

# Create a method called get_groups that prints the animal/animals inside each group.
    def show_animals(self):
        return animal_list
    
animals_list = []
animal1 = Zoo('cow')
animal2 = Zoo('bear')

# Create an object called ramat_gan_safari and call all the methods. 
# Tip: The zookeeper is the one who will use this class.

class ramat_gan_safari():
    
    dir(Zoo)   
  
user = Zoo('Zookeeper')

user.new_animal= animal1
print(animals_list)


    

             
        