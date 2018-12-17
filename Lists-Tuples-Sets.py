
# use the following format to create lists ['','',''] etc.
courses = ['history', 'math', 'physics', 'CompSci']

print (courses)
print (len(courses))
# you can use -1 to get the last item
print (courses[0:3]) 

# Append to add an item to list
courses.append('art')
print(courses)

# use insert to insert an item into a list at a specific location
courses.insert(0, 'science')
print(courses)

#use extend to add new things to a list
courses_2 = ['biology', 'education']
courses.extend(courses_2)
print(courses)

# Removing values from a list
courses.remove('math')
print(courses)

# Reverse 
courses.reverse()
print (courses)

# Sort
courses.sort()
print (courses)
nums = [1, 5 , 2 ,6 ,3]
nums.sort()
print (nums)
# Reverse Sort 
nums.sort(reverse=True)
print(nums)

# Min to find minumum number in list
print(min(nums))
# Max to find maximum number in list
print (max(nums))
# Sum to find sum of numbers in list
print (sum(nums))

#to find the index of use index and search
print(courses.index('CompSci'))

# To check if a value is in the list use "in" operator
print('art' in courses)

# to loop through values in a list use "for" loop
for course in courses:
	print(course)
# to find the index of what value youre on use the "enumerate" function
for index, course in enumerate (course, start=1):
	print(index, course)

# To turn string into list 
course_str = ' - '.join(courses)
print(course_str)

# Sets
cs_courses = {'history', 'math', 'physics', 'CompSci',}
art_courses = {'history', 'math', 'art', 'design'}
print (cs_courses)
print ('math' in cs_courses)

# intersection method is used to find common stuff in different sets
# difference is used to find stuff that aren't in common
# union is to combine both sets
print (cs_courses.intersection(art_courses))
print (cs_courses.difference(art_courses))
print (cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This atually creates an empty dictionary
empty_set = set()


