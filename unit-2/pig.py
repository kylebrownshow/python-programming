pig_players = ['p1', 'p2']

p1_total = 0
p2_total = 0

max_score = 25

import random

print(f'welcome to pig. roll the die to add to your score.  but beware: roll a 1, and your score goes to 0.')
turn = 1

while True:
    if p1_total >= max_score:
        print('player 1 wins - you fucking did it!')
        break
    elif p2_total >= max_score:
        print('player 2 wins - revel in this victory!')
        break
    else:
        dice_total = random.randint(1,6)
        choice = input('press \'r\' to roll or \'p\' to pass the die: ')
        if choice == 'r':
            print(f'{dice_total} was rolled')
            if dice_total != 1:
                if turn == 1:
                    p1_total += dice_total
                    print(f'p1 score is {p1_total}, p2 score is {p2_total}')
                else:
                    p2_total += dice_total
                    print(f'p1 score is {p1_total}, p2 score is {p2_total}')
            else:
                if turn == 1:
                    p1_total = 0
                    print(f'p1 score is {p1_total}, p2 score is {p2_total}')
                    print('p1 loses turn. score returned to 0. p2 rolls')
                    turn = 2
                else:
                    p2_total = 0
                    print(f'p1 score is {p1_total}, p2 score is {p2_total}')
                    print('p2 loses turn. score returned to 0. p1 rolls')
                    turn = 1
        else:
            if turn == 1:
                print(f'p1 score is {p1_total}, p2 score is {p2_total}') 
                print('p1 passes. p2 rolls')
                turn = 2
            else:
                print(f'p1 score is {p1_total}, p2 score is {p2_total}')
                print('p2 passes. p1 rolls')
                turn = 1