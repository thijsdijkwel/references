
num = 1 

# to figure out whether a number is an integer or float:
print(type(num))

# Arithmetic Operators:
# Addition:       3 + 2 
# Substraction:   3 - 2
# Multiplication  3 * 2
# Division:       3 / 2
# Floor Division  3 // 2 
# Exponent        3 ** 2 
# Modulus         3 % 2   (finds the remainder)
   # examples:
print (3 + 2)
print (3 % 2)
print (8 // 2)

# absolute value
print (abs(-3))

# use round to round a number. add a comma and integer to choose how many values to round it to 
print(round(3.75, 1))

# Comparisons: (boolean)
# Equal:             3 == 2
# Not Equal:         3 != 2
# Greater than:      3 > 2
# Less Than:         3 < 2
# Greater or Equal:  3 >= 2
# Less or Equal:     3 <= 2

num_1 = 3
num_2 = 2
print (num_1 == num_2)
print (num_1 != num_2)

#Casting (change from string to integer)
num_3 = '100'
num_4 = '200'
num_3 = int(num_3)
num_4 = int(num_4)

print(num_3 + num_4)