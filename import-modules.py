# Come back to this later when you have a better grasp on everything as a whole.
# Python Tuturial for beginners 9: Import Modules and Exploring The Standard Library
print ('imported my module...')

test = 'Test String'


def find_index (to_search, target):
	''' Find the index of a value in a sequence '''
	for i, value in enumerate (to_search):
		if value == target:
			return i

		return -1

