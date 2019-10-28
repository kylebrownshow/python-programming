#for all numbers from 1 to 50
#if its a multiple of 3, print 'fizz'
#if its a multiple of 5, print 'buzz'
#if its a multiple of 15, print 'fizzbuzz'
#otherwise print the number

for num in range(1, 51):
    if num % 15 == 0:
        print('fizzbuzz')
    elif num % 5 == 0:
        print('buzz')
    elif num % 3 == 0:
        print('fizz')
    else:
        print(num)