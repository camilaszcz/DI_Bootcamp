# Using the input function, ask the user for a string. The string must be 10 characters long.
from calendar import c


string = input('Give me a 10 letter word!')
# If it’s less than 10 characters, print a message which states “string not long enough”.
if len(string)<10:
    print('Word not long enough')
    # If it’s more than 10 characters, print a message which states “string too long”.
elif len(string)>10:
    print('Word too long')
    # Then, print the first and last characters of the given text.
else:
    print('First char:', string[0])
    print('Last char:', string[-1])
    # temp_str=''
    # for x  in string:
    #     temp_str+=c
    #     print(temp_str)
        
    for i in range(len(string)):
        print(string[:i+1])
    


