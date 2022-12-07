class MovieReview:
    def __init__(self, movie, story, actors, music):
        #Movie Name
        self.movie_name = movie

        #Movie Ratings
        self.story_rating = story
        self.actors_rating = actors
        self.music_rating = music

        self.avg = int((self.story_rating + self.actors_rating + self.music_rating)/3) 

        self.myrating = {
            "Movie Name": self.movie_name,
            "Story Rating": self.story_rating,
            "Actor Rating": self.actors_rating,
            "Music Rating": self.music_rating,
            "Average Rating": self.avg
        }

    def ratings(self,movieRatings):
        movieRatings.append(self.myrating)
    
    def get_star(self, movieRatings):
        for movie in movieRatings:
            if(movie["Average Rating"]==1):
                print("Thanks for your response, You rated the movie with *")
                print(movie)
            elif(movie["Average Rating"] == 2):
                print("Thanks for your response, You rated the movie with **")
                print(movie)
            elif(movie["Average Rating"] == 3):
                print("Thanks for your response, You rated the movie with ***")
                print(movie)
            elif(movie["Average Rating"] == 4):
                print("Thanks for your response, You rated the movie with ****")
                print(movie)
            else:
                print("Thanks for your response, You rated the movie with *****")
                print(movie)
    
moviereviews = []
review2 = MovieReview("Beautiful Sound", 5, 5, 5)
review2.ratings(moviereviews)
review2.get_star(moviereviews)