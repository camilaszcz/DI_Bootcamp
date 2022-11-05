# Challenge 1

length = int(input('Provide a length'))

value = int(input('Provide a number'))


def multiples(value, length):
    return [*range(value, length*value+1, value)]

print(multiples(value, length))


# Challenge 2

# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

user_word=input('Tell me a word')

def removeConsecutiveDuplicates(s):
    if len(s) < 2:
        return s
    if s[0] != s[1]:
        return s[0]+removeConsecutiveDuplicates(s[1:])
    return removeConsecutiveDuplicates(s[1:])

print(removeConsecutiveDuplicates(user_word)) 
  