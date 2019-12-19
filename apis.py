#use the requests module

import json
import requests

response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

data = response.json() #this variable can be called anything

#print(data) #this will dirty print the data
#print(json.dumps(data,indent=4)) #this pretty prints the result

print(response) #this will return 404 for an error or 200 for success

print(data.keys()) # this returns the keys in a dictionary and gives us an idea of what we're looking at

print(type(data['teams']))

print(data['teams'][0])

#look at the first item in this list

#we can pretty print again
#print(json.dumps(data['teams'][0], indent = 4))

#save to a file
with open('nhl.json', 'w') as nhl_file:
    nhl_file.write(json.dumps(data))

print("done...")
