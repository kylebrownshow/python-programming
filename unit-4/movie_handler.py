#import json
#movie_list = 'movies.json'

class Movie:
    def __init__(self, title, genre, running_time, movie_cast):
        self.title = title
        self.genre = genre
        self.running_time = running_time
        self.movie_cast = movie_cast

    def add_cast(self, actor):
        self.actor = actor
        self.movie_cast.append(actor)
        print (f'{actor} added.')

    def describe(self):
        print (f'{self.title} is a {self.genre} that runs {self.running_time} minutes.  It stars {self.movie_cast}.')

#    def load_movies(self):
#        #load the data from the movies.txt file  
#        with open(movie_list, 'r') as movies: #as defined on line 1
#            data = json.load(movies)
#        #set the movies variable to the data loaded in
#        self.movies = data

    def compare_to(self,movie1):
        for actor in self.movie_cast:
            count = 0
            if actor == movie1.movie_cast[actor]:
                count +=1
        if count < 2:
            print (-1)
        else: 
            print (1)


labyrinth = Movie("Labyrinth", "Fantasy", 101, ["Jennifer Connelly", "David Bowie", "Toby Froud"])
labyrinth.describe()
labyrinth.add_cast("Brian Henson")
labyrinth.describe()

littleshop = Movie("Little Shop of Horrors", "Sci-Fi", 104, ["Ellen Greene", "Rick Moranis", "Steve Martin", "Levi Stubbs"])
parenthood = Movie("Parenthood", "Comedy Drama", 124, ["Joaquin Phoenix", "Keanu Reeves", "Steve Martin", "Rick Moranis"])

labyrinth.compare_to(littleshop)