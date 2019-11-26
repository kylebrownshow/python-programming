#sets do not allow duplicates

#sets also use curly brackets like dictionaries

rainbow_colours = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}

print(type(rainbow_colours))

#the line above is a set, and python doesn't know until we add values to it (it might think that it's a dictionary)

#a set is like a list without duplicates.  and we can make a set from a list.  

values = [1, 5, 7, 3, 5, 5, 9, 7]

unique_values = set(values)

print(unique_values)

#sets are not ordered like lists are: an item is either in the set or it is not. 

#we use .append to add to a list, but we use .add to add to a set.  

unique_values.add(5)

#we can remove from a set with .remove

unique_values.remove(3)

#note that python won't complain if we add a duplicate value to a set.  it will just skip over it.

print(unique_values)

#unique_values.remove(3)  #if we try to remove something that isn't there, we will receive a keyerror

#single line is_isogram

def is_isogram(string):
    return len(set(string)) == len(string)

#OR
#    unique = set(string)
#    if len(unique) == len(string):
#        return True
#    else:
#        return False

#tuples are a specific type of list, like strings, that are immutable (you can't reassign items).  we create them with parentheses.

#tuples are ordered.  we can have duplicates in a tuple, but we can't change them

weekdays = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')

#python won't let you do this: weekdays[6] = 'Dom', but you can still use the index to find a specific position

print(weekdays[0])