print('Python pizza delivery')

size = input('What size? S, M or L?')
pepperoni = input('Y or N?')
extra_cheese = input('Y or N?')

price = 0

if size == 'S':
    price += 10
elif size == 'M':
    price += 15
else: price += 20

if pepperoni == 'Y':
    price += 3

if extra_cheese == 'Y':
    price += 2

print(f'Your pizza will cost £{price}')

name = input('Customer name?')

if name != 'Ned' and name != 'Toby':
    print('Here is your order pal!')
elif name == 'Ned':
    print('Okally-dokally, Ned!')
elif name == 'Toby':
    print('Here is your pizza Toby')