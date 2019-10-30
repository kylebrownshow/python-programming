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
'''
values = [2.3, 45, 11, -5, 3.5, 7.9, 11.7, 40, 85.6, 77.1]
float_list = []

for num in values:
    if type(num) is float:
        float_list.append(num)

print (float_list)

''' also correct answer, because if the number isn't odd or even, it must be a float

for num in values:
    if num % 2 != 1 and num % 2 !=0:
        float_list.append(num)

print (float_list)

'''