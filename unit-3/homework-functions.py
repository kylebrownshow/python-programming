#Write a function called reverse_list that accepts a list, and returns a copy of the list with the items in reverse order

def reverse_list(original_list):
    pos = len(original_list) - 1
    newlist = []
    while pos >= 0:    
        newlist.append(original_list[pos])
        pos -= 1

    print(newlist)

#Write a function called encode_string that accepts a string of letters, and returns a new string with the letters replaced as their corresponding number position in the alphabet 

def encode_string(string):
    numera = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26')
    alpha = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    new_string = ''
    string_pos = 0
    alpha_pos = 0
    while string_pos <= len(string) - 1:
        if string[string_pos] == alpha[alpha_pos]:
            new_string += numera[alpha_pos]
            string_pos += 1
            alpha_pos = 0
        else:
            alpha_pos += 1

    print(new_string)

#Write a function called pivot_split that accepts two arguments: a list of integers and an integer, called pivot.  Return list [(with numbers <),(numbers with => pivot)]

def listsplitter(wholelist):
    pivot = 20
    ween = []
    biggun = []
    whole = [25, 36, -42, -16, 0, 125, 88, 1, 4, 17]

    for num in whole:
        if num < pivot:
            ween.append(num)
        else:
            biggun.append(num)

    print(ween)
    print(biggun)
