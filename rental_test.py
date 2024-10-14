import unittest
from rental import Rental
from movie import Movie
from price_strategy import *


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", NewReleasePrice())
        self.regular_movie = Movie("Air", RegularPrice())
        self.children_movie = Movie("Frozen", ChildrenPrice())

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", RegularPrice())
        self.assertEqual("Air", m.get_title())
        self.assertEqual(RegularPrice(), m.get_price_strategy())

    def test_get_price(self):
        """Test to check whether get_price works correctly."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_price(), 3.5)

        rental = Rental(self.children_movie, 1)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.children_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        """Test to check whether rental_points works correctly."""
        rental = Rental(self.new_movie, 3)
        self.assertEqual(rental.get_rental_points(), 3)

        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_rental_points(), 1)

        rental = Rental(self.children_movie, 3)
        self.assertEqual(rental.get_rental_points(), 1)
