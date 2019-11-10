countries = ['Mexico', 'Mexico', 'Jamaica', 'French Polynesia', 'USA', 'Thailand', 'Greece', 'Philippines', 'Puerto Rico', 'Jamaica']
destinations = ['Cozumel', 'Cancun', 'Montego Bay', 'Bora Bora', 'Maui', 'Phuket', 'Mykonos', 'Palawan', 'Vieques', 'Negril']

for idx in range(len(destinations)):
    destinations[idx] += ' - ' + countries[idx]

print(destinations)