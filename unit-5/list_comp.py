#list comprehension can be used to create a new list from an existing one

master_nums = [1,3,6,8,9,11,15,18]

#create a new list with only the even numbers

even_nums = []
for num in master_nums:
    if num % 2 == 0:
        even_nums.append(num)

#list comprehension can do this in one line

new_even_nums = [num for num in master_nums if num % 2 == 0]

print(new_even_nums)

#best way to construct a list comprehension: append, loop, condition, 

#a list with the square of the even numbers

even_square_list = [value * value for value in master_nums if value % 2 == 0]

print(even_square_list)

#create a list of the titles with 't' in their names

titles = ['lord of the rings', 'the time machine', 'the great gatsby', 'moby dick', 'chronicles of narnia']

titles_with_t = [book for book in titles if 't' in book]
print(titles_with_t)

#convert a string to uppercase
string = 'i am the best'
#creates a lkist of the characters in uppercase
capital_string = ''.join([char.upper() for char in string])

print(capital_string)

result = ''