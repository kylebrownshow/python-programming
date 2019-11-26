import json

#create a class, and make the class name capital
class Person:
    #every class must have an init method.  and it must be written particularly with two underscores (also called a "dunder method")
    # a method is a special kind of function that is defined within a class, and is defined within the class
    # only python calls the dunder method.  users don't have to do it.
    # the init "initializes" the data that is required for it. 
    def __init__(self, n, a):
        #('person object initialized')
        #in this case, 'self' is a way to keep track of its own self.  we use self to instantiate data.  always self.
        #we choose the name of data with the suffix on the left.  
        self.name = n
        self.age = a

    def say_hello(self):
        print(f'Hello my name is {self.name} and I am {self.age} years old')

#functions within a class don't always have to use 'self' - but if they don't, they can't use the class data

#how to instantiate (create an instance of) a class (create an object).  until we instantiate, we've only created a template.
#we have to instantiate outside of the block.  can't instantiate inside the block: that would be circular.

p = Person('John', 35)
q = Person('Jane', 28)

print(p.name)
print(q.name)

#use a class method with .
p.say_hello()

print(type(p))

#create a rectangle class
#it should have a length and a width
#it should have two methods: perimeter and area

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def perimeter(self):
        return (self.width + self.width + self.length + self.length)

    def area(self):
        return (self.length * self.width)

r1 = Rectangle(4, 10)
r2 = Rectangle(8, 4)

print(f'Area of r2 is {r2.area()}, perimeter is {r2.perimeter()}.')

#create a playlist class that has a name and a list of tracks
#each track is really a dictionary, with title, artists, length of track

#write methods to add a track, to remove a track, to shuffle the playlist

track_file_name = 'tracks.json'

class Playlist:
    def __init__ (self, name): #no need to include the empty list, because it's empty and that's obvious
        self.name = name
        self.playlisttracks = [] #we can declare the 

    def add_track(self, title, artist, length):
        track = {}
        track['title'] = title
        track['artist'] = artist
        track['length'] = length
        self.playlisttracks.append(track)

    def remove_track(self, title):
        for idx in range(len(self.playlisttracks)):
            if title == self.playlisttracks[idx]['title']:
                break
        self.playlisttracks.pop(idx)

    def save_tracks(self):
        #open file for writing
        with open(track_file_name, 'w') as track_file:
            track_file.write(json.dumps(self.playlisttracks))

    def load_tracks(self):
        #load the data from the tracks.txt file  
        with open(track_file_name, 'r') as track_file: #track_file_name on line 60
            data = json.load(track_file)
        #set the tracks variable to the data loaded in
        self.playlisttracks = data

new_playlist = Playlist('new music')
new_playlist.load_tracks()
print(new_playlist.playlisttracks)

#player = Playlist('tunes')
#player.add_track ('solisbury hill', 'peter gabriel', 4.23 )
#player.add_track ('real real gone', 'van morrison', 3.38 )
#player.add_track ('all you need is love', 'the beatles', 3.53 )
#player.save_tracks()

# we want to write the tracks to properly formatted json