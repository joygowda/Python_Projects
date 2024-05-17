dictionary = {
                "cat": "chat", 
                "dog": "chien", 
                "horse": "cheval"
                }
phone_numbers = {'boss' : 5551234567, 
                    'Suzy' : 22657854310
                }
                
empty_dictionary = {}

words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
