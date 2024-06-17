"""
Tuple
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
"""

#Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""
Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
Allow Duplicates
Since tuples are indexed, they can have items with the same value:
"""

#Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

#What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#<class 'tuple'>

#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

LIST is a collection which is ordered and changeable. Allows duplicate members.
TUPLE is a collection which is ordered and unchangeable. Allows duplicate members.
SET is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
DICTIONARY is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""

#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#Packing a tuple:

fruits = ("apple", "banana", "cherry")

#Unpacking a tuple:

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

"""
Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.
Example
Print all items by referring to their index number:
"""
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

"""
Using a While Loop
You can loop through the tuple items by using a while loop.
Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
Remember to increase the index by 1 after each iteration.
Print all items, using a while loop to go through all the index numbers:
"""
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Tuple Methods
#Python has two built-in methods that you can use on tuples.

count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found




