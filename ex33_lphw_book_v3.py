"""
Exercise 33:While-Loops from Book: Learn Python the Hard Way, Third Edition by Zed A. Shaw
Coded by Joy Dhairyalakshmi Gowda
"""
i = 0
numbers = []

#while 1 < 6: #Creates infinite loop
for i in range (0, 10):
    print("At the top 1 is %d" % i)
    numbers.append(i)

    print("Numbers now: ", numbers)
    print("At the bottom is %d" % i)

print("The numbers:")
for num in numbers:
    print(num)