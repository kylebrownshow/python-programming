cohort_4 = ['kyle', 'allaina', 'chizea', 'christina', 'daniela', 'emma', 'julian', 'keerthi', 'sahil', 'shilaj', 'lizhi']

'''print (len(cohort_4))

#access items in list using position (index)

print (cohort_4)

print (cohort_4[0])

#use type to find class.  classes have functions that are associated with them. we call these methods. 

print (type(cohort_4))

#append is a list method that adds to the end of a list.

cohort_4.append('princeton')

print (cohort_4)

#remove an item from a list with remove

cohort_4.remove('julian')
print (cohort_4)

#valueerror return when we try to remove a value from a list that is not there 
cohort_4.remove('julian')

#create a new list with only the floats

values = [2.3, 45, 11, -5, 3.5, 7.9, 11.7, 40, 85.6, 77.1]
float_list = []

for num in values:
    if type(num) is float:
        float_list.append(num)

print (float_list)

also correct answer, because if the number isn't odd or even, it must be a float

for num in values:
    if num % 2 != 1 and num % 2 !=0:
        float_list.append(num)

print (float_list)


#find average of each list and add to a new list

weights = [[50, 25, 75], [95.7, 38.3, 55.2], [88, 45, 16]]

new_list = []

for item in weights:
    list_total = 0
    for value in item:
        list_total += value
    
    new_list.append(list_total/len(item))
    
print(new_list)


#using the same theory of loops within loops, output 
*
**
***
****
*****
******
*******
********
*********
**********

for row in range(1, 11):
    for col in range (1, row + 1):
        print('*', end=' ')
    print('')


for i in range(11):
    print('*' * (i+1))


#using indexes to access list items
#use index if we need to edit items in list

#set all the negative readings to 0
'''
readings = [3.5, -7.7, -9.8, 13.6, 22.5, 19.7, -8.6]

for idx in range(len(readings)):
    if readings[idx] < 0:
        readings[idx] = 0
print(readings)

#find the position of an item in a list

current_age = 25
ages = [15, 17, 27, 35, 12, 25, 55, 40, 31, 20]

for idx in range(len(ages)):
    if ages[idx] == current_age:
        print('25 is found at position ', idx)