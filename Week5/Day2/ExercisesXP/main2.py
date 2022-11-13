# 🌟 Exercise 3 : Dogs Domesticated

# Instructions

# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.


from main import Dog
import random

class PetDog(Dog):

    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dogs):
        out = f"{self.name}, "
        for i, dog in enumerate(dogs):
            if i == len(dogs) - 1:
                out += f"{dog.name} ALL PLAY TOGETHER"
            else:
                out += f"{dog.name}, "
        print(out)

    def do_a_trick(self):
        if self.trained:
            tricks = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']
            random_trick = random.choice(tricks)
            print(f"{self.name} {random_trick}")
        else:
            print(f"{self.name} is not trained!")

dog1 = Dog('Bon', 5, 10)
dog2 = Dog('Pickle', 2, 10)
dog3 = Dog('Rex', 1, 8)

petdog = PetDog('Kashyo', 2, 7)

petdog.play(dog1, dog2, dog3)
petdog.do_a_trick()