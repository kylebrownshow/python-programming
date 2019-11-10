#function to add two integers
def add(num1, num2):
    return num1 + num2

#python will print nothing at this point, because the function has yet to be called.  also: the function is just holding variables with no value (we declare them later)
'''
print(add(5,10)) #this calls the function within print

result = add(50,20) #this assigns the function to a variable
'''
#this function displays hello there
def say_hello():
    print('Hello There!')

#function that returns the length of a string

def length(string):
    return len(string)

#function to return the sum of integers in a list
def sum_of_integers(a_list):
    result = 0
    for num in a_list:
        if type(num) is int:
            result += num

    return result

#function to reverse a string

def revstring(string):
    idx = len(string) - 1
    rev_string = ''
    while idx >= 0:
        rev_string += string[idx]
        idx -= 1

    return rev_string
    
#reverse string in one line (python)

def one_line_reverse(string):
    return string[::-1]

#  :: means "from first to last".  ::-1 means "from last to first"

#using a for loop - Daniela's solution

def daniela_reverse(string):
    result = ''
    for char in string:
        result = char + result

        return result
