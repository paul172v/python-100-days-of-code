import random

friends = ['Sarian', 'Toman', 'Gabriel', 'Serrano']
num = random.randint(0,3)

### Method 1
print(friends[num])

### Method 2
print(random.choice(friends))

food = [['pork', 'beef', 'chicken'], ['salmon', 'tuna', 'haddock']]
print(random.choice(food[0]), random.choice(food[1]))