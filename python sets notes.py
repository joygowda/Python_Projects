#Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

"""
Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.
"""

#example: duplicate values ignored

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#example: True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#Example: False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#example: Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Example:Set items can be of any data type.String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#Example: A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

#What is the data type of a set? <class 'set'>

myset = {"apple", "banana", "cherry"}
print(type(myset))

#Example: Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Example: Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Example: Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#To add items from another set into the current set, use the update() method.
#Example: Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

"""
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
Add any iterable.
Example:Add elements of a list to at set:
"""

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Remove Item: To remove an item in a set, use the remove(), or the discard() method.

#Example: Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Example:Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

"""
Note: If the item to remove does not exist, discard() will NOT raise an error.
You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
The return value of the pop() method is the removed item.
Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
"""

#Example: Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

"""
Join Sets
There are several ways to join two or more sets in Python.
The union() and update() methods joins all items from both sets.
Note: Both union() and update() will exclude any duplicate items.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

#Example:Join set1 and set2 into a new set:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#You can use the | operator instead of the union() method, and you will get the same result.
#Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the union() method.
#example: Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#Join multiple sets with the union() method:
#Note: Both union() and update() will exclude any duplicate items.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

#Note: Both union() and update() will exclude any duplicate items.
#Join a set with a tuple:

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

"""
Update
The update() method inserts all items from one set into another.
The update() changes the original set, and does not return a new set.
Note: Both union() and update() will exclude any duplicate items.
"""

#Example: The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Intersection
#Keep ONLY the duplicates
#
#The intersection() method will return a new set, that only contains the items that are present in both sets.

#Example: Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#You can use the & operator instead of the intersection() method, and you will get the same result.
#The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
#Example: Use & to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

"""
The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
The values True and 1 are considered the same value. The same goes for False and 0
"""

#Example: Keep the items that exist in both set1, and set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
#Example: Keep all items from set1 that are not in set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

#You can use the - operator instead of the difference() method, and you will get the same result.
#Use - to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

#Use the difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
#Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

#Keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
#Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
#Use ^ to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)


#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
#Use the symmetric_difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)


