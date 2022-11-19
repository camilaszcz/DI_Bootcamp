# Part 1 : Quizz :

# Answer the following questions

# # What is a class?
# A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods. 
# # What is an instance?
# An instance is a specific realization of any object. An object may be different in several ways, and each realized variation of that object is an instance. The creation of a realized instance is called instantiation.
# # What is encapsulation?
# It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.
# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
# # What is abstraction?
# It hides the unnecessary code details from the user. Also,  when we do not want to give out sensitive parts of our code implementation and this is where data abstraction came.
# # What is inheritance?
# Inheritance is the capability of one class to derive or inherit the properties from another class. The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class
# # What is multiple inheritance?
# Multiple level inheritance enables one derived class to inherit properties from more than one base class.
# # What is polymorphism?
# Polymorphism simply means having many forms. For example, we need to determine if the given species of birds fly or not, using polymorphism we can do this using a single function.
# # What is method resolution order or MRO?
# Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute. Python supports classes inheriting from other classes. The class being inherited is called the Parent or Superclass, while the class that inherits is called the Child or Subclass.



# The Deck of cards class should NOT inherit from a Card class.

import random
from random import shuffle

class Cards:
    global suites, values
    suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  
    def __init__(self):
        pass
    
    # def show(self) :
    #     print (f'{self.value} of {self.suit}')

# Creation of card class is done; by creating an instance of a class, we can test this.
# card = Card('Cards',6)
# card.show()


# I couldnt find a solution that the deck does not inherit from class card

class Deck(Cards):
    def __init__(self):
        Cards.__init__(self)
        self.mycardset = []
        for n in suites:
            for c in values:
                self.mycardset.append((c)+" "+"of"+" "+n)
        
# Method to remove a card from the deck
    def popCard(self):
        if len(self.mycardset) == 0:
            return "NO CARDS CAN BE POPPED FURTHER"
        else:
            cardpopped = self.mycardset.pop()
            print("Card removed is", cardpopped)
  
    # Define a class to shuffle the deck of cards
class ShuffleCards(Deck):
  
    def __init__(self):
        Deck.__init__(self)
  
    # Method to shuffle cards
    def shuffle(self):
        if len(self.mycardset) < 52:
            print("cannot shuffle the cards")
        else:
            shuffle(self.mycardset)
            return self.mycardset
  
    # Method to remove a card from the deck//// pop=deal
    def popCard(self):
        if len(self.mycardset) == 0:
            return "NO CARDS CAN BE POPPED FURTHER"
        else:
            cardpopped = self.mycardset.pop()
            return (cardpopped)



objCards = Cards()
objDeck = Deck()
  
# Player 1
player1Cards = objDeck.mycardset
print('\n Player 1 Cards: \n', player1Cards)
  
# Creating object
objShuffleCards = ShuffleCards()
  
# Player 2
player2Cards = objShuffleCards.shuffle()
print('\n Player 2 Cards: \n', player2Cards)
  
# Remove some cards
print('\n Removing a card from the deck:', objShuffleCards.popCard())
print('\n Removing another card from the deck:', objShuffleCards.popCard())
            





