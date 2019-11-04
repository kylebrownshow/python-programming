temperature_readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]

pos_list = []
neg_list = []

pos_list_total = 0
neg_list_total = 0

#average_of_positive_readings
#average_of_negative_readings

for num in temperature_readings:
    if num >= 0:
        pos_list.append(num)
        pos_list_total += num 
    else:
        neg_list.append(num)
        neg_list_total -= num
    

print(f'the average of positive readings: {pos_list_total / len(pos_list)}')
print(f'the average of negative readings: {neg_list_total / len(neg_list)}')

print(neg_list_total)
print(pos_list_total)