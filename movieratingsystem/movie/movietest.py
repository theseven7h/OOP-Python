import unittest

from movieratingsystem.movie.movie import Movie

class MovieRatingSystemTest(unittest.TestCase):
    def setUp(self):
        self.movie = Movie("movieName", [])

    def test_movie_name_is_correct_at_initialisation(self):
        name = self.movie.get_name()
        self.assertEqual(name, "movieName")

    def test_movie_rating_is_correct(self):
        rating = self.movie.get_all_ratings()
        self.assertEqual(rating, [])



if __name__ == '__main__':
    unittest.main()
