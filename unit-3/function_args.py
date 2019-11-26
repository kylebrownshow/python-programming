#args* means "print all the arguments you'd like!"
# we have to include the * when we are defining the argument, but we can't add the asterisk again when we call it in a loop

def add(*args):
    total = 0
    for item in args:
        total += item

    return total

print(add(1,2,3,4,5,6,7,8,9,10))