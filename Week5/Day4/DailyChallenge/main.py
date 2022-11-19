# Instructions :



# Part I

# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”
# a method to return the frequency of a word in the text (assume words are separated by whitespace)
# a method that returns a list of all the unique words in the text.



# unique
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] > 1
            pass
        else:
            counts[word] = 1

    return counts

print( word_count('A good book would sometimes cost as much as a good house.'))

# frequency
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count('A good book would sometimes cost as much as a good house.'))



# a method that returns the most common word in the text.
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] <= 0
            pass
        else:
            max(counts[word])
    return counts

print(word_count('A good book would sometimes cost as much as a good house.'))

# the KeyError is the most common word in the string


# didnt have time to finish the second part
# Part II

# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


# Now, use the provided the_stranger.txt file and try using the class you created above.



