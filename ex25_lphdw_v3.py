"""
Exercise 25 from Book: Learn Python the Hard Way v3
Coded by Joy Dhairyalakshmi Gowda
"""

sentence = "All good things come to those who wait."

def break_words(sentence):
    print("""This function will break up words for us.""")
    words = sentence.split(' ')
    return words

def sort_words(words):
    print(""" Sorts the words.""")
    return sorted(words)

def print_first_word(words):
    print("""prints the first word after popping it off.""")
    #word = words.pop(0) pop() canot be used for strings
    print(words)

def print_last_word(words):
    print(""" Prints the last word after popping it off.""")
    #words = words.pop(-1) pop() cannot be used for strings
    print(words)

def sort_sentence(sentence):
    print("""Takes in a full sentence and returns the sorted words.""")
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    print(""" Prints the first and last words of the sentence.""")
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    print(""" Sorts the words then prints the first and last one.""")
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

break_words(sentence)
sort_words(sentence)
#print_first_word(sentence)
print_last_word(sentence)
sort_sentence(sentence)
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)