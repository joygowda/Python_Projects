"""
Exercises from book Learn Python the Hard Way, version 3, adapted to Python 3
by Joy Dhairyalakshmi Gowda

I never got the message from 2011, but I may have figured it out PART of story somewhat.
I liked computer programming most. I can work remotely to prevent gossip from interfering with my ability to work.
Fill your team with an unusual and independent thinker. Hire me. 

"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

"""
Other escape chacters for refernce from Python docs: Section 2.4.1.1. Escape sequences

\<newline>   Backslash and newline ignored

\\ Backslash (\)

\' Single quote (')

\" Double quote (")

\a ASCII Bell (BEL)

\b ASCII Backspace (BS)

\f ASCII Formfeed (FF)

\n ASCII Linefeed (LF)

\r ASCII Carriage Return (CR)

\t ASCII Horizontal Tab (TAB)

\v ASCII Vertical Tab (VT)

\ooo  Character with octal value ooo

\xhh Character with hex value hh

Escape sequences only recognized in string literals are:

\N{name}  Character named name in the Unicode database

\uxxxx   Character with 16-bit hex value xxxx

\Uxxxxxxxx Character with 32-bit hex value xxxxxxxx
"""
