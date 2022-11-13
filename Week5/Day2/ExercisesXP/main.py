# Exercise 1 : Pets

# Using this code:

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'



# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : 
# one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value 
# is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.


# 🌟 Exercise 2 : Dogs

# Create a class called Dog with the following attributes name, age, weight.

# class Dog:
#   def __init__(self, name, age, weight):
#     self.name = name
#     self.age = age
#     self.weight = weight
    
# # Implement the following methods in the Dog class:
# # bark: returns a string which states: “<dog_name> is barking”.

#   def myfunc(self):
#     print(self.name + " is barking.")

# dog1 = Dog("Samson", 1, 10)
# dog1.myfunc()


# # run_speed: returns the dogs running speed (weight/age*10).
# # fight : takes a parameter which value is another Dog instance, called other_dog. 
# # This method returns a string stating which dog won the fight. 
# # The winner should be the dog with the higher run_speed x weight.
# # Create 3 dogs and run them through your class.


# class Dog:

#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         return f"{self.name} is barking"

#     def run_speed(self):
#         return (self.weight/ self.age) * 10

#     def fight(self, other_dog):
#         # run_speed x weight
#         this_dog_strength = self.run_speed() * self.weight
#         other_dog_strength = other_dog.run_speed() * other_dog.weight
#         winner = self if this_dog_strength > other_dog_strength else other_dog

#         return f"{winner.name} has Won!"


# if __name__ == '__main__': 

#     print("RUNNING CODE DIRECTLY (Without import)")
#     dog1 = Dog('Bon', 5, 10)
#     dog2 = Dog('Pickle', 2, 10)
#     dog3 = Dog('Rex', 1, 8)

#     # dogs = [dog1, dog2, dog3]

#     print(dog2.fight(dog3))