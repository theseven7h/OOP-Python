from datetime import datetime, timedelta

class MovieRatingSystem:
    def __init__(self, movies: list):
        self.movies = movies

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_date(self):
        date = datetime.today()
        return date.strftime("%B %d, %Y at %I:%M%p")

    def get_added_movies(self):
        return self.movies

    def validate_rating(self, rating):
        rating_out_of_range = rating < 1 or rating > 5
        if rating_out_of_range: raise ValueError("Rating must be between 1 and 5")

    def add_rating(self, movie_name, rating):
        self.validate_rating(rating)
        for movie in self.movies:
            if movie.get_name() == movie_name:
                movie.get_all_ratings().append(rating)

    def get_movie(self, movie_name):
        for movie in self.movies:
            if movie.get_name() == movie_name:
                return movie
        return None

    def get_average_rating(self, movie_name):
        movie = self.get_movie(movie_name)
        ratings = movie.get_all_ratings()
        return sum(ratings) / len(ratings)
