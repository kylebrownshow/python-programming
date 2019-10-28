
#write a program to calculate the sum of all even numbers between 1000 and 10000
#the program should print 'the sum of even numbers between 1000 and 10000 is ___"

total = 0

for num in range (1000,10001):
    if num % 2 == 0:
        total += num
    
        print (f'the sum of even numbers between 1000 and 10000 is: {total}')

