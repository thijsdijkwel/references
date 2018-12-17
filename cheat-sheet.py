# message is a variable 
message = ('Hello World')

# Length 
# to get the length, follow this format:
print(len(message))

# Slicing and Index
# to find location (index) follow this format:
# the starting point is the 0, the colon signifies the stopping point. 
    
print(message[0:5]) 

# Lowercase method
# to change an entire message to lowercase, follow this format.
print(message.lower())

# Count
# use this function to count the amount of a certain character
print(message.count('o'))

# Find
# This function is used to find a certain character
print (message.find('l'))

# Replace
# This method replaces a string of characters
# Must set a new variable to get a return string with the replacements
new_message = message.replace('World','Universe')
print (new_message)

#Concatenating Strings
# Assign variables and use + signs
greeting = 'Hello '
name = 'Thijs'
third_message = greeting + name
print (third_message)

# dir function
# dir function gives you a broad overview of all the methods available 
print (dir(name))

# Help function
# gives you more information on what a specific function does.
# replace 'str' with any other method or function 
print (help(str))

# thank you jason