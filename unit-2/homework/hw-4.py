string = 'Python Programming at General Assembly is Awesome!!'
phrase = ''

for char in string:
    if char != ' ' and char !='s' and char != 'm':
        phrase += char

print (phrase)
