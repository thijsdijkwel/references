# Comparisons: (boolean)
# Equal:              == 
# Not Equal:          != 
# Greater than:       > 
# Less Than:          < 
# Greater or Equal:   >= 
# Less or Equal:      <= 
# Object Identity:    is

language = 'Java'

if language == 'Python':
	print ('Language is Python')
# the elif statement is used as an additional 'if'
elif language == 'Java':
	print ('Language is Java')
elif language == 'Ruby':
	print ('Language is Ruby')
# Else is used as a null. If none of the conditions are met, else statement will print
else: 
	print ('No match')

a = [1, 2, 3]
b = [1, 2, 3]
# is figues out the ID of a function
# you can use the ID function shown below to find exact ID
print (id(a))
print (id(b))
print (a == b)
print (a is b)


# and - both need to be true
# or - only one needs to be true
# not - changes true to false and false to true

user = 'Admin'
logged_in = True 

if user == 'Admin' and logged_in:
	print ('Admin Page')
else:
	print ('Insufficient Credentials')

# example of not function
if not logged_in:
	print ('Please log in')
else:
	print ('Welcome')

# False Values:
	# False
	# None
	# Zero of any numeric type
	# Any empty sequence. For exmaple, '', (), [.
	# Any empty mapping. For example, {}.
condition = 'Test'

if condition:
	print('Evaluated to True')
else: 
	print ('Evaluated to False')