#ClassExercise

# Given this list:


# list1 = [5, 10, 15, 20, 25, 50, 20]


# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value


# Hint : Look at the index method


    
list1 = [5, 10, 15, 20, 25, 50, 20]

# get the first occurrence index
index = list1.index(20)

# update item present at location
list1[index] = 200
print(list1)

#difference of list and tuple:
#tuble is not changable

#Difference between tuple and list:

#tuple is between () or nothing
#list is between []

#Sets definition
set = {1,2,3}  #set type
set = {} #empty is a dict type

