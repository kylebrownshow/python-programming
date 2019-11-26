import json #java script object notation.  json files are lightweight, decently readable, and can be read by any browser 

person = {'Name': 'Alice', 'Job': 'Engineer', 'city': 'Toronto'}

print(type(person))

#properly formatted json must have
#keys and all strings enclosed in double quotations
#enclosed with curly brackets, square brackets can be used to enclose a list of objects

with open('cohort_4.json','r') as cohort_file:
    cohort = json.load(cohort_file) #converts json file to python dictionary, which makes it way easier to read than if we just printed from the json
    #this is important, because it makes the json folder searchable

print(type(cohort))
#print(cohort) returns a convoluted result that is difficult to read, and has no breaks
print(json.dumps(cohort, indent=2)) #indents are useful for making the output easier to read.  there are no rules, but 2 or 4 is enough.  
