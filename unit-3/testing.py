original_list = ['kristen', 'graeme', 'kyle', 'lindsay', 'colin', 'iain', 'scott', 'olivia', 'georgia']
newlist = []
pos = len(original_list) - 1

while pos >= 0:    
    newlist.append(original_list[pos])
    pos -= 1

print(newlist)

string = 'happy'
numera = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

string_pos = 0
alpha_pos = 0
new_string = ''

while string_pos <= len(string) - 1:
    if string[string_pos] == alpha[alpha_pos]:
        new_string += numera[alpha_pos]
        string_pos += 1
        alpha_pos = 0
    else:
        alpha_pos += 1

print(new_string)

#Write a function called pivot_split that accepts two arguments: a list of integers and an integer, called pivot.  Return list [(with numbers <),(numbers with => pivot)]

