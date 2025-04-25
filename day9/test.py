list = []

list.append({'name':'Sarian', 'age': 23})
list.append({'name':'Gabriel', 'age': 28})
list.append({'name':'Toman', 'age': 32})
list.append({'name':'Serrano', 'age': 42})

highest_age = 0
oldest_character = 'placeholder'

for dictionary in list:
   if dictionary['age'] > highest_age:
        oldest_character = dictionary['name']

print(f"{oldest_character} is the oldest")

    