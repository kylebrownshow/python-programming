phrases = ['you always tip your server 20%, because youve been there', 'you are the type of person that signals before turning', 'you have great hair, but you havent let it get to your head', 'you only squish bugs when theyre being gross', 'people say nice things about your penmanship']

import random

while True:
    answer = input('enter your name (or type e to exit)')
    if answer == 'e':
        break
    else: 
        print(phrases[random.randint(0,4)])


#import random
#Princeton's solution programmatically knows the length of the list
#Princeton also uses \ to indicate escape characters so he can push apostraphe's into his strings like this 'you\'re' 

#name = input('please enter your name (or e to end):')
#messages = ['you\'re awesome', 'have a great day', 'you\'re a party animal']

#while name!= 'e':
#    pos = random.randint(0, len(messages) - 1)
#    print(messages[pos])
#    name = input('Please enter your name 9or e to end): ')