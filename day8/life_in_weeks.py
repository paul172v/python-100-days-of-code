age = int(input('What is your age?'))

def life_in_weeks(age):
    weeks_in_year = 4 * 12
    time_left = weeks_in_year * age
    print(f'{time_left} weeks remaining.')

life_in_weeks(age)
