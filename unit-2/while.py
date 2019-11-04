#while loop starts only when a condition is met

import random #random number module


val = 1

while val < 10:
    print(val)
    val += 1 #increment val


#guessing game

guess = int(input('guess my number (1 - 10) '))
# answer = 7
answer = random.randint(1,10)

while guess != answer:
    guess = int(input('guess again, sucka! '))

print('you got it!')

#how do you break a loop?

names = ['jack', 'jill', 'mary', 'jane', 'kate']

idx = 0

while idx < len(names):
    if names[idx] == 'mary':
        print('found Mary!')
        break
    idx += 1

#how do we loop forever

while True:
    answer = input('continue(y/n)')
    if answer == 'n':
        break
