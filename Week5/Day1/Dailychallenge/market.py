# Take a look at the following code and output:
# File: market.py


# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

    

# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)

      
# def get_info(self):
#     print('')

# print(macdonald.get_info(self))

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.


# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_details(self):
#     print("Hello my name is " + self.name)

# first_person = Person("John", 36)
# first_person.show_details()




# Farm

class Farm(object):
    def __init__(self, name, anthem):
        self.name = name
        self.anthem = anthem
    
    def say_name(self):
        print(self.name)
    
    def say_anthem(self):
        print(self.anthem)
        
        # def get_info(self):
        #  print(self.info)
        
macdonald = Farm('McDonald', 'E-I-E-I-0!')
# macdonald.get_info(f'{self.name}'Farm' + {Animal.self.name} + '=' {Animal.self.quantity})

# Animals
class Animal(Farm):
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

        Animal.__init__(self, name, quantity)

            
#Create an animal
animal_1 = Animal("Cow", 1)
animal_2 = Animal('Goat', 1)
animal_3 = Animal('Sheep', 1)

macdonald.say_name()

# print(Farm.get_info(self))


# ////completely stuck, will request help from the TA !!!!