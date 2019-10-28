'''
total = 14


# a single = is an assignment.  Two equal signs are required to look for equality

if total ==15:
  print('good')
else:
  print('you have made me very upset')

if total % 2 ==1:
  print('odd')
else:
  print('even')

name = 'kyle'

if len (name) > 7:
  print('this is a nice size')
else:
  print('this is suboptimal size')


#print corresponding letter for a grade
# if score is 80 - 100, print 'A'
# if score is 60 - 79, print 'B'
# if score is 50 - 69, print 'C'
# otherwise, print F

#comparison operators 
# == equal
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# != not equal to


grade = 69

if grade <= 50:
    print('Fail')
elif grade <= 69:
    print('C')
elif grade <= 79:
    print('B')
else:
    print('A')

'''

#a non-empty string is 'Truthy'
if 'hello world':
  print('yes its true')

#an empty string is 'Falsey'
if'':
  print('its true')
else:
  print('it is false')

#any number that is not zero is truthy
if 13:
  print('it is true')

#0 is falsey
if 0:
  print('it is true')
else:
  print('it is false')

a = -10
b = -17

if a > 0 or b < 0:
  print('good!')

if a > 0 and b < 0:
  print('excellent')
else:
  print('why have you done this')