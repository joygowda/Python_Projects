"""
Much longer form of adventure prompt game inspired by
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
    elif bear == "3":
        print("Welcome home! You're safe. Go get some soda and take a nap.")
    elif bear == "4":
        print("Sorry, Firefly is no longer on the air. Go to bed. ")
    elif bear == "42":
        print("The answer is not 42 here. But the bear sits down and wants to hear the story.")
    elif bear == "7":
        print("So smart you are, you ran away from the bear!")
    elif bear == "8":
        print("Ok, but that book doesn't matter now,does it? The bear ate both hands. \nYou can't dial for help and it's a long walk. Let's get started. ")
    elif bear == "9":
        print("The giant bear killed you immediately. You have earned a good reincarnation, so let's go there now!")
    elif bear == "0":
        print("The operator cannot help you. Please the program over.")
    elif bear == "2371":
        print("No, this isn't Voyager taking off. You lost a lot of blood and you are in shock. Call 911 now.")
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
    elif insanity == "3":
        print("You scared Cthulhu! How is that possible? Go see a plastic surgeon as soon as you can. You need an estimate."              )
    elif insanity == "42":
        print("Too bad. The answer is not 42 here. You died. Start over.")
    elif insanity == "5":
        print("Yes, you made the living ship mad, so she showed you this. Find out what she really wants now. ")
    elif insanity == "9":
        print("How fortunate you are that you just woke up from a nightmare!")
    elif insanity == "7":
        print("You died immediately. Good job! Welcome to your afterlife! ")
    elif insanity == "0":
        print("Welcome home. Go drink some water, maybe log off and get some rest. You had a tough day. ")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job. At least you can still see while you insane!")

else:
    print("You stumble around and fall on knife and die. Welcome to discussion about your reincarnation.")