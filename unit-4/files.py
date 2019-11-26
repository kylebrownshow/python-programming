#how to read a file

my_file = open('lines.txt', 'r') #without a full file path, python will assume that the file is in the same folder as the python script

#my_file = open('C:/Users/Kyle.Brown/python-programming/unit-1/hello.py', 'r')

#r is for reading, w is for writing, a is for appending

data = my_file.read()

my_file.close() #you should close a file after using it

print(data)

#how to we write a file

my_file = open('lines.txt', 'w') #w overwrites the contents of the file if it exists. 
my_file.write('please add this new line')
my_file.close()

my_file = open('new_lines.txt', 'w') #w also creates when the commanded file doesn't exist 
my_file.write('lines for my new file')
my_file.close()

#to add to the end of file, use append (a)

my_file = open('new_lines.txt', 'a')
my_file.write('\nnew file should have new line as well')
my_file.close()

#we can use 'with' if we don't want to have to close every time

with open('lines.txt', 'r') as text_file: #we use with so that we don't need to use open and close.  note the alias created! 
    data = text_file.read() #note how the command uses the new alias!

print(data)

#TLDR: use with and scrap that open & close business