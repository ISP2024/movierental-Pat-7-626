import unittest
from rental import Rental
from movie import Movie
from pricing import *


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie(title="Dune: Part Two", year=2020, genre=["Action", "Adventure", "Fantasy"])
        self.regular_movie = Movie(title="Air", year=2002, genre=["Action", "Fantasy"])
        self.children_movie = Movie(title="Frozen", year=2016, genre=["Adventure", "Fantasy"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        self.assertEqual("Air (2002)", self.regular_movie.get_title())

    def test_get_price(self):
        """Test to check whether get_price works correctly."""
        rental = Rental(self.new_movie, 1, NewReleasePrice())
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5, NewReleasePrice())
        self.assertEqual(rental.get_price(), 15.0)

        rental = Rental(self.regular_movie, 1, RegularPrice())
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 3, RegularPrice())
        self.assertEqual(rental.get_price(), 3.5)

        rental = Rental(self.children_movie, 1, ChildrenPrice())
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.children_movie, 5, ChildrenPrice())
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        """Test to check whether rental_points works correctly."""
        rental = Rental(self.new_movie, 3, NewReleasePrice())
        self.assertEqual(rental.get_rental_points(), 3)

        rental = Rental(self.regular_movie, 3, RegularPrice())
        self.assertEqual(rental.get_rental_points(), 1)

        rental = Rental(self.children_movie, 3, ChildrenPrice())
        self.assertEqual(rental.get_rental_points(), 1)
