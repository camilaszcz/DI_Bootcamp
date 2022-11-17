import math

# Create a class called Farm. How should it be implemented?

class Farm():
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animal_list = {}

    def add_animal(self, animal_name, animal_quantity=1):
        if animal_name in self.animal_list:
            current_quantity = self.animal_list[animal_name]
            self.animal_list[animal_name] = current_quantity + animal_quantity  
        else:
            self.animal_list[animal_name] = animal_quantity
                               
    def anthem(self,anthem):
        self.anthem = anthem

        
# Output

macdonald = Farm("McDonald")
print(macdonald.farm_name +'\'s farm')

# McDonald's farm
        
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.animal_list)



anthem = 'E-I-E-I-0!'
print(anthem)

# print(macdonald.get_info())




