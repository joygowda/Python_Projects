"""
Exercises from book Learn Python the Hard Way, version 3, adapted to Python 3
by Joy Dhairyalakshmi Gowda

I never got the message from 2011, but I may have figured out PART of story somewhat.
They gave someone wrong woman but she used my name and SSN that year to plot revenge, since families didn't really matter to them and they didn't want Hindu family reunited.
They kept me from working since 2018 with gossip on Facebook.
They knew I tested for programming aptitude in 1999 but resented me for ability to earn $.
Vaughn F. said it was Anne Keller who ran brothels BUT I wasn't ever her!
I worry because I think my kids were tricked to trash a good mother, but nobody would tell me. 

"""
#data from book includes
#my_name = 'Zed A. Shaw'
#my_age = 35 #not a lie
#my_height = 74 #inches
#my_weight = 180 #lbs
#my_eyes = 'Blue'
#my_teeth = 'White'
#my_hair = 'Brown'

#created dictionary with keys and values
person = {'my_name': 'Zed A. Shaw', "my_age": 35, "my_height": 74, "my_weight": 180, "my_eyes": "blue", "my_teeth": "white", "my_hair": "brown"}

print(f"Let's talk about" {my_name}".".format(**person))
print(f"He's"{my_height}" inches tall.").format(**person)
print(f"He's" {my_weight}" pounds heavy.").format(**person)
print("Actually that's not too heavy.")
print(f"He's got" {my_eyes}" eyes and "{my_hair}"hair.").format(**person)
print(f"His teeth are usually "{my_teeth}" depending on the coffee.").format(**person)


#fixing f-string issues later. finding challenges in finding right syntax that will work in my iDE

