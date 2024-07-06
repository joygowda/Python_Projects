"""
Exercise 31:Making Decisions from Book: Learn Python the Hard Way v3 by Zed A. Shaw
Coded by Joy Dhairyalakshmi Gowda
"""

print("You enter a dark room with two doors. Do you go through door number 1 or door number 2.")

door = input(">>>>>> ")

if door == "1":
    print("There's a giant bear sitting here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">>>>>>   ")

    if bear == "1":
        print("The bear eats your face off. Nothing to do but think about every mistake in life as you bleed to death. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Too bad but at least the bear walks away and you can call for help!")
    elif bear == "7":
        print("So smart you are, you ran away from the bear!")
    else:
        print("Well, doing %s is probably better. Bear runs away. ") %bear

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">>>>>>   ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Tough luck.")
    elif insanity == "9":
        print("How fortunate you are that you just woke up from a nightmare!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job. At least you can still see while you insane!")

else:
    print("You stumble around and fall on knife and die. Welcome to discussion about your reincarnation.")