import json

with open('nhl.json', 'r') as nhl_file:
    data = json.load(nhl_file) #this will convert the json file into a python dictionary or list as long as there is no formatting error in the json file

print(data.keys()) #.keys analyzes as if the object is a dictionary.  if this was a list, we might check for its length.

#this step is important for explorartory purposes.  we want to get an idea of the elephant we're trying to eat!

#how many teams are in the nhl?

print(len(data['teams']))


#when were the bruins founded

teams = data['teams']
eastern_teams = []
first_years = []
oldest_team = ''
oldest_year = 2019

#when were the bruins founded

for element in teams:
    if element['locationName'] == "Boston":
        print(element['firstYearOfPlay'])

#what are all of the teams in the eastern conference

for element in teams:
    if element['conference']['name'] == "Eastern":
        eastern_teams.append(element['teamName'])

print(eastern_teams)

#what is the oldest team in the NHL

for element in teams:
    first_years.append(int(element['firstYearOfPlay']))
    oldest = min(first_years)
    if element['firstYearOfPlay'] == str(oldest):
        oldest_team = element['teamName']

print(f'the {oldest_team} are the NHL\'s oldest team.  They were founded in {oldest}.')