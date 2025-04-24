print('Tip calculator')

bill = float(input('What is the bill?'))
tip = int(input('What are you tipping?'))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

number_of_people = int(input('How many people?'))
total_per_person = total_bill / number_of_people

print(f'Each person should pay £{total_per_person}')