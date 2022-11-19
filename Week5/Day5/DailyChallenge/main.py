# Using the requests and time modules, create a function which returns the 
# amount of time it takes a webpage to load (how long it takes for a complete 
# response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

# Importing the libraries
from urllib.request import urlopen
from time import time

# Obtaining the URL of website
website = urlopen('https://www.geeksforgeeks.org/')

# Return the number of seconds
# passed since epoch
open_time = time()

# Read the complete website
output = website.read()

# Return the number of seconds
# passed since epoch
close_time = time()

# Close the website
website.close()

# Subtract and print the open time
# of website from close time
print('The loading time of website is',round(close_time-open_time,3),'seconds')


# Obtaining the URL of website
website = urlopen('https://stackoverflow.com/')

# Return the number of seconds
# passed since epoch
open_time = time()

# Read the complete website
output = website.read()

# Return the number of seconds
# passed since epoch
close_time = time()

# Close the website
website.close()

# Subtract and print the open time
# of website from close time
print('The loading time of website is',round(close_time-open_time,3),'seconds')


# Obtaining the URL of website
website = urlopen('https://www.google.com/')

# Return the number of seconds
# passed since epoch
open_time = time()

# Read the complete website
output = website.read()

# Return the number of seconds
# passed since epoch
close_time = time()

# Close the website
website.close()

# Subtract and print the open time
# of website from close time
print('The loading time of website is',round(close_time-open_time,3),'seconds')


# Obtaining the URL of website
website = urlopen('http://learn.di-learning.com/')

# Return the number of seconds
# passed since epoch
open_time = time()

# Read the complete website
output = website.read()

# Return the number of seconds
# passed since epoch
close_time = time()

# Close the website
website.close()

# Subtract and print the open time
# of website from close time
print('The loading time of website is',round(close_time-open_time,3),'seconds')

# Results:
# geekeforgeeks
# The loading time of website is 0.033 seconds
# stackoverflow
# The loading time of website is 0.63 seconds
# google
# The loading time of website is 0.013 seconds
# developers institute
# The loading time of website is 0.002 seconds

