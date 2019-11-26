def frequency_counter(string):
    unique_count_dict = {}

    for letter in string:
        unique_count = 1
        if letter in unique_count_dict:
            unique_count_dict[letter] += 1
        else:
            unique_count_dict[letter] = 1
            unique_count_dict[letter] = unique_count

    return unique_count_dict
    
print (frequency_counter('happy'))

#def frequency_counter(string):
#    result = {}
#    for char in string:
#        if char in result:
#            result[char] += 1
#        else:
#            result[char] = 1
#    return result
#
#print(frequency_counter('happy'))

def lists_to_dict(peoplejobs):

    new_dictionary = {}
    
    for double in peoplejobs:
        new_dictionary[double[0]] = double[1]     
    
    return (new_dictionary)

people = ([['name', 'Alice'], ['job', 'Engineer'], ['city', 'Toronto']])
    
print(lists_to_dict(people))

