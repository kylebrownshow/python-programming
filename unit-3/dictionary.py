#a dictionary is a collection of key/value pairs
# dictionaries use curly brackets {  }  .  sets also use curlies, but we're not talking about that right now.

student = {'name': 'emma', 'age': 25, 'address': 'Toronto'}

#access elements in a dictionary

print(student['name'])
print(student['address'])
print(student['age'])

#a dictionary cannot have duplicate keys
#add items to a dictionary

car = {} #creates an empty dictionary like '' defines an empty string and [] defines an empty list

car['make'] = 'Toyota'
car['model'] = 'Prius'
car['year'] = 2019
car['colour'] = 'silver'

print(car) #note that this computer's version of python uses ordered dictionaries

car['year'] = 1997 #entering this key in twice overwrites the previous value.  that's why it's best practice to not use keys twice.

print(car)

#how do we iterate over a dictionary
for item in car:

#if we ever do the "for in" on a dictionary, we'll get back the keys (not the values)

    print(item) #this returns the keys
    print(car[item]) #this returns the values

#challenge: make a list of dictionaries

cars = [{'make': 'Toyota', 'model': 'Prius', 'year': 1997, 'colour': 'silver'},{'make': 'Chevy', 'model': 'Aveo', 'year': 2006, 'colour': 'black'},
{'make': 'Lincoln', 'model': 'Navigator', 'year': 2010, 'colour': 'red'}, {'make': 'Chevy', 'model': 'Blazer', 'year': 2011, 'colour': 'black'},
{'make': 'Ford', 'model': 'Bronco', 'year': 1990, 'colour': 'blue'}]

#how do we process a list of dictionaries?

count = 0

for vehicle in cars:
    if vehicle['make'] == 'Chevy':
        count += 1

'''
{
    '_id': 100,
    'year': 2019,
    'title': 'Bodak Yellow',
    'artist': {
        'name': 'Cardi B'}

    }
    'tracks': [
        {
            '_id': 100,
            'title':
        }
    ]
}
'''

print(count)

#the return for car is a dictionary, because - in this case - cars is a list of dictionaries.  so print(car) would return a list of dictionaries

#write a function called frequency counter that returns the frequency of each letter in the string

#def frequency_counter(string)

#frequency_counter('a testy line of text')

'''
'a': 1
' ': 4
't': 4
'e': 2
's': 1
'y': 1
'l': 1
'i': 1
'n': 1
'o': 1
'f': 1
'x': 1
'''

#use a dictionary
#use the keys method to get the keys of a dictionary

print(car.keys())

#use the values method to get the values of a dictionary

print(car.values())

#use the items method to get both the keys and values of a dictionary 

print(car.items())

for key, value in car.items():
    print(key, value)