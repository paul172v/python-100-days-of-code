import random

cpu = ['rock', 'paper', 'scissors']
cpu_choice = random.choice(cpu)
## print('CPU picks ' + cpu_choice)

player_choice = input('rock, paper, scissors?')
print('Player picks ' + player_choice)

if cpu_choice == 'rock' and player_choice == 'paper':
    print('Player wins!!!')
elif cpu_choice == 'paper' and player_choice == 'scissors':
    print('Player wins!!!')
elif cpu_choice == 'scissors' and player_choice == 'rock':
      print('Player wins!!!')
elif cpu_choice == 'rock' and player_choice == 'rock':
    print('Draw!!!')
elif cpu_choice == 'paper' and player_choice == 'paper':
    print('Draw!!!')
elif cpu_choice == 'scissors' and player_choice == 'scissors':
    print('Draw!!!')
else:
    print('CPU wins!!!')