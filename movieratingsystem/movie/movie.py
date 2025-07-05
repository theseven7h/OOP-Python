# from datetime import datetime, timedelta

class Movie:
    def __init__(self, name, rating):
        self.movie_detail = {"name": name, "ratings": rating}

    def get_name(self):
        return self.movie_detail['name']

    def get_all_ratings(self):
        return self.movie_detail['ratings']



