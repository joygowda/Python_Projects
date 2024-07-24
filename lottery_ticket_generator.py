"""
Lottery ticket generator
Coded by Joy Dhairyalakshmi Gowda
No guarantee to win or promises, since I haven't won any games. Someone just says stuff online to harass me.
Finished project will match Powerball draws
Will be coded to add comparisons with Powerball API and user selected numbers and attractive display
as I learn more Python
"""

import random


def gen_ticket():
	numbers = []
	count = 0
	while count < 6:
		numbers.append(random.randint(1,69))
		count += 1
	return numbers

print(gen_ticket())

