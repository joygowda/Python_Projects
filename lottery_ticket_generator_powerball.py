"""
Lottery ticket generator for Powerball
Coded by Joy Dhairyalakshmi Gowda
No guarantee to win or promises, since I haven't won any games. Someone just says mean stuff online to harass me.
The REAL story involves apartment mailbox pried open for a week in middle to end of Februuary 2011 in Phoenix, AZ, so I assume the sender spend the $.
Finished project will add statistics with Powerball API, allow user selected numbers and
add GUI as I learn more Python.
"""

import random


def gen_ticket():
	numbers = []
	count = 0
	while count < 6:
		numbers.append(random.randint(1,69))
		count += 1
	return numbers

def powerball():
	number = random.randint(1,26)
	return number

print(gen_ticket())
print(powerball())

