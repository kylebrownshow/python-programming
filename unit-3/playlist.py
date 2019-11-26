playlist =[{'title': 'days gone down', 'genre' : 'jazz rock', 'artist': 'gerry rafferty', 'year': '1979', 'length' : 6.28 },
{'title': 'operator', 'genre' : 'rock', 'artist': 'jim croce', 'year': '1972', 'length' : 3.25  },
{'title': 'st judys comet', 'genre' : 'easy listening', 'artist': 'paul simon', 'year': '1973', 'length' : 3.22 },
{'title': 'wild world', 'genre' : 'pop', 'artist': 'cat stevens', 'year': '1970', 'length' : 3.20 },
{'title': 'rhiannon', 'genre' : 'rock', 'artist': 'fleetwood mac', 'year': '1975', 'length' : 4.10  },
{'title': 'nothing left to lose', 'genre' : 'rock', 'artist': 'alan parsons project', 'year': '1980', 'length' : 4.05  },
{'title': 'sister golden hair', 'genre' : 'rock', 'artist': 'america', 'year': '1975', 'length' : 3.17 },
{'title': 'solisbury hill', 'genre' : 'pop', 'artist': 'peter gabriel', 'year': '1977', 'length' : 4.23  },
{'title': 'real real gone', 'genre' : 'pop', 'artist': 'van morrison', 'year': '1990', 'length' : 3.38  },
{'title': 'all you need is love', 'genre' : 'rock', 'artist': 'the beatles', 'year': '1967', 'length' : 3.53 }]

def titles(playlist):
    for song in playlist:
        print (song['title'])

def artists(playlist):
    for song in playlist:
        print (song['artist'])

def playlength(playlist):
    playlistlength = 0
    for song in playlist:
        playlistlength += (song['length'])


#while True:
#    choice = input('Do you want to see Titles, Artists or playlength?')
#    if choice == 'titles' or 'Titles':
#        print titles()


