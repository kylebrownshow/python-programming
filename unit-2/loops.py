'''
#the for loop
name = 'kyle'

for num in range(1,11):
    if num % 2==1:
        print(num)

#for all of the numbers in the following range, print the name variable
total=0

for num in range(1,11):
    if num % 2==0:
       total += num

print(total)

#store your full name in a variable
#loop over your name
#print each vowel in your name

name = 'kyle brown'
vowel = 'a' or 'e' or 'i' or 'o' or 'u'

for char in name:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print(char)

'''  

my_numbers = [3, 5, 17, 11, 21, 53, -10, -27, 45, 80]
smallest_number = my_numbers[0]

for num in my_numbers:
    if num < smallest_number:
        smallest_number = num

print (smallest_number)
