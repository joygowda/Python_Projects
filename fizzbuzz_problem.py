"""
Fizz Buzz Problem states that given an integer n, for every integer i <= n, the task is to print “FizzBuzz” if i is divisible by 3 and 5, 
“Fizz” if i is divisible by 3, “Buzz” if i is divisible by 5 or i (as a string) if none of the conditions are true.
"""
for i in range (100):
	if i % 3 == 0 and i % 5 == 0:
 		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
else:
	print ("i") 
