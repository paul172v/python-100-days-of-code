import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]

player_hand = []
cpu_hand = []
game_over = False 

def calc_highest():
    total_points_player = sum(player_hand)
    total_points_cpu = sum(cpu_hand)

    if total_points_player > total_points_cpu:
        game_over == True
        return print(f"Player wins with a score of {total_points_player} to CPU's score of {total_points_cpu}")
    elif total_points_cpu > total_points_player:     
        game_over == True
        return print(f"CPU wins with a score of {total_points_cpu} to Player's score of {total_points_player}!")
    elif total_points_cpu == total_points_player:
        game_over == True
        return print('Draw')

    

def calc_points(hand, user):
    total_points = 0
      
    total_points = sum(hand)

    if total_points > 21:
        for card in hand:
            if card == 11:
                card = 1
                return calc_points(hand, user)
            else:
                return print(f'{user} is over 21, you lose!')
    elif total_points == 21:
       return print(f"{user} has 21, {user} wins!")
    elif total_points < 21:
        if (game_over == False):
            print(player_hand)
            draw_new_card = input('Draw new card?')

        if (draw_new_card == 'yes'):
            drawCard(hand, user)
            draw_new_card = ''
            return calc_points(hand, user)
        elif (draw_new_card == 'no'):
            draw_new_card = ''
            return calc_highest()


def initialDeal(hand):
    card1 = random.choice(deck)
    card2 = random.choice(deck)

    hand.append(card1)
    hand.append(card2)

def drawCard(hand, user):
    card = random.choice(deck)
    hand.append(card)
    calc_points(hand, user)

initialDeal(player_hand)
initialDeal(cpu_hand)

calc_points(player_hand, 'Player')



