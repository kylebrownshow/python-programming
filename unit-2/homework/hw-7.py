phrases = ['you always tip your server 20%, because youve been there', 'you are the type of person that signals before turning', 'you have great hair, but you havent let it get to your head', 'you only squish bugs when theyre being gross', 'people say nice things about your penmanship']

import random

while True:
    answer = input('enter your name (or type e to exit)')
    if answer == 'e':
        break
    else: 
        print(phrases[random.randint(0,4)])

