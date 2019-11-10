#strings are immutable

movie_title = "Thor, the Dark World"

print(movie_title[0])

#what we cannot do is change the elements of a string outside of the string

#movie_title[5] = '-'

#what we CAN do is reassign the string by declaring it again

movie_title = 'The Avengers'

#a string like this will pull specific characters from another string

start = movie_title[0:2]

#we can use negatives to look back to grab characters from the end of a string

print(start)

print(movie_title[-1:-9])

print(movie_title[2:])

#use the colon to drive a command that looks from a certain character to the end of a string, or from the beginning to a specific character