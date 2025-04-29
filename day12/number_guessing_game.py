import random

NUMBER = random.randint(1,100)
tries = 5

def guess(tries):
    if (tries == 0):
        print('Out of tries, you lose!')
    elif (tries > 0):
        
        guessed_number = input('Guess the number between 1-100....')       
        if (guessed_number == NUMBER):
            return print('Congrats, you guessed correctly!')
        elif (guessed_number != NUMBER):
            tries -= 1
            print(f"{tries} tries remaining!")
            guess(tries)

guess(tries)


## constant variables are written in capitals