
nums = [1, 2, 3, 4, 5]
# Break keyword completely breaks out of a loop
# Continue keyword moves onto the next iteration of the loop

for num in nums:
	if num == 3:
		print ('found!')
		break
		# because the first 2 didn't meet the conditional, it didn't print "found!"
		# but once it did hit 3, it found it and printed found and then broke.
	print (num)

for num in nums:
	if num == 3:
		print ('found!')
		continue
		# using continue caused it to continue the loop
	print(num)

# loop in a loop
for num in nums:
	for letter in 'abc' :
		print (num, letter)

# to go through a loop a certain number of times
for i in range(10):
	print(i)
# if you want to start at 1:
for i in range (1,11):
	print(i)

#While loops will continue until a break or until a condition is met
x = 0

while x < 10:
	if x == 5:
		break
	print (x)
	x += 1

# to create an infinite loop, use true
while x < True:
	if x == 10:
		break
	print #(x)
x += 1 