#1. How many customers are there in all? 
# 2. Print the name and email address of the customer with id 13 
# 3. Print all the items ordered by the customer with id 20. 
# 4. How may customers bought wine? 
# 5. What is the total cost of the items ordered by Matti? 
# 6. Which customer spent the most money on orders?

import json

order_file = 'orders.json'

class Orders:
    def __init__ (self, id, customer_name, customer_email, orders): #no need to include the empty list, because it's empty and that's obvious
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.orders = orders
        self.customer_orders = [] 

    def load_orders(self):
        #load the data from the tracks.txt file  
        with open(order_file, 'r') as order_file: #track_file_name on line 60
            data = json.load(order_file)
        #set the tracks variable to the data loaded in
        self.customer_orders = data

    def count_customers(self):
        count = 0
        for customer in customer_name:
            count += 1
        print (count)

order_list = Orders('new orders')
order_list.load_orders()
print(order_list.Orders)
