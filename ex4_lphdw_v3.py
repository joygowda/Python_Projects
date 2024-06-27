"""
Exercises from book Learn Python the Hard Way, version 3, adapted to Python 3
by Joy Dhairyalakshmi Gowda

I never got the message from 2011, but I may have figured it out PART of story somewhat.
They gave __ Peaches Adams that year to plot revenge, families didn't really matter to them and they didn't want family reunited.
She wasn't college student, but they don't value college, or me. They kept me from working since 2018 with gossip on Facebook.

"""
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people, today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")