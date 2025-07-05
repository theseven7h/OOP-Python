import unittest

from movieratingsystem.movie.movie import Movie
from movieratingsystem.ratingsystem.ratingsystem import MovieRatingSystem


class TestMovieRatingSystem(unittest.TestCase):
    def setUp(self):
        self.rating_system = MovieRatingSystem([])

    def test_movie_can_be_added(self):
        self.movie = Movie("movieName", [])
        self.rating_system.add_movie(self.movie)
        name = self.movie.get_name()
        rating = self.movie.get_all_ratings()

        self.assertEqual(name, "movieName")
        self.assertEqual(rating, [])

    def test_length_is_1_when_1_movie_is_added(self):
        self.movie = Movie("movieName", [])
        self.rating_system.add_movie(self.movie)

        added_movies = self.rating_system.get_added_movies()
        self.assertEqual(len(added_movies), 1)

    def test_multiple_movies_can_be_added(self):
        self.movie = Movie("movieName", [])
        self.rating_system.add_movie(self.movie)

        added_movies = self.rating_system.get_added_movies()
        self.assertEqual(len(added_movies), 1)

        name = self.movie.get_name()
        rating = self.movie.get_all_ratings()

        self.assertEqual(name, "movieName")
        self.assertEqual(rating, [])

        self.movie_2 = Movie("movieName2", [])
        self.rating_system.add_movie(self.movie_2)

        added_movies = self.rating_system.get_added_movies()
        self.assertEqual(len(added_movies), 2)

        name = self.movie_2.get_name()
        rating = self.movie_2.get_all_ratings()

        self.assertEqual(name, "movieName2")
        self.assertEqual(rating, [])

    def test_can_add_ratings_to_movie(self):
        self.movie = Movie("movieName", [])
        self.rating_system.add_movie(self.movie)

        self.rating_system.add_rating("movieName", 4)
        self.assertEqual(self.rating_system.get_movie("movieName").get_all_ratings(), [4])

    def test_can_add_multiple_ratings_to_a_movie(self):
        self.movie = Movie("movieName", [])
        self.rating_system.add_movie(self.movie)

        self.rating_system.add_rating("movieName", 4)
        self.rating_system.add_rating("movieName", 2)
        self.rating_system.add_rating("movieName", 3)
        self.assertEqual(self.rating_system.get_movie("movieName").get_all_ratings(), [4,2,3])

    def test_average_ratings_for_a_movie_is_correct(self):
        self.movie = Movie("movieName", [])
        self.rating_system.add_movie(self.movie)

        self.rating_system.add_rating("movieName", 4)
        self.rating_system.add_rating("movieName", 2)
        self.rating_system.add_rating("movieName", 3)

        self.assertEqual(self.rating_system.get_average_rating("movieName"), 3)

    def test_exception_raised_when_rating_lower_than_1_or_greater_than_5(self):
        self.movie = Movie("movieName", [])
        self.rating_system.add_movie(self.movie)

        self.assertRaises(ValueError, self.rating_system.add_rating, "movieName", 7)

    def test_exception_message_when_rating_lower_than_1_or_greater_than_5(self):
        self.movie = Movie("movieName", [])
        self.rating_system.add_movie(self.movie)

        with self.assertRaises(ValueError) as err:
            self.rating_system.add_rating("movieName", 7)
        self.assertEqual(str(err.exception), "Rating must be between 1 and 5")


if __name__ == '__main__':
    unittest.main()
