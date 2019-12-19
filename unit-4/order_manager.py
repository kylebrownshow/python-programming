#1. How many customers are there in all? 
# 2. Print the name and email address of the customer with id 13 
# 3. Print all the items ordered by the customer with id 20. 
# 4. How may customers bought wine? 
# 5. What is the total cost of the items ordered by Matti? 
# 6. Which customer spent the most money on orders?

import json

with open('orders.json', 'r') as order_file:
    customer_orders = json.load(order_file)
        #set the tracks variable to the data loaded in

print(type(customer_orders))

#print(customer_orders)
#1. How many customers are there in all? 

def counter(orders):
    count = 0
    for item in orders:
        count += 1
    return count

print(f'there are {counter(customer_orders)} customers')


#2. Print the name and email address of the customer with id 13 

for cus in customer_orders:
    if cus['id'] == 13:
        print (cus['customer_name'], cus['customer_email'])

#3. Print all the items ordered by the customer with id 20. 

for cus in customer_orders:
    items = []
    if cus['id'] == 20:
        for order in cus['orders']:
            items.append(order['item'])
        print (items) 

#4. How may customers bought wine? 
#for cus in customer_orders:
#    winecount = []
#    for item in cus['orders']:
#        if item['items'] == "wine"

#5. What is the total cost of the items ordered by Matti? 
for cus in customer_orders:
    count = 0
    if cus['customer_name'] == "Matti":
        for price in cus['orders']:
            count += float(order['price'].replace('$',''))
        print(count)

#6. Which customer spent the most money on orders?

for cus in customer_orders:
    count = 0
    if cus['customer_name'] == "Matti":
        for price in cus['orders']:
            count += float(order['price'].replace('$',''))
        print(count)