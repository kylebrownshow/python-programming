#

def encode_string(string):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    result = ''
    for char in string:
        for idx in range(len(alpha)):
            if char == alpha[idx]:
                result += str(idx + 1)

    print(encode_string('happy'))

#pivot

def pivot_split(my_list, my_num):
    left = []
    right = []
    for num in my_list:
        if num < my_num:
            left.append(num)
        else:
            right.append(num)

    return [left, right]

def frequency_counter(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

print(frequency_counter('happy'))