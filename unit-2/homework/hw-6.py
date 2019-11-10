marvel_movies = ['iron man', 'the amazing spiderman', 'the incredible hulk', 'Thor', 'Captain America: The FIrst Avenger', 
'Guardians of the Galaxy', 'Ant-Man', 'Doctor Strange', 'Black Panther', 'Black Widow']
special_marvel_movies = []

for flick in marvel_movies:
    if 'the ' in flick:
        special_marvel_movies.append(flick)

print(special_marvel_movies)