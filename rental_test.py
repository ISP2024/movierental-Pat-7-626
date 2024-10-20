import unittest
from rental import Rental
from pricing import *


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie(title="Latest Blockbuster", year=datetime.now().year, genre=["Action"])
        self.regular_movie = Movie(title="Classic Film", year=1995, genre=["Drama"])
        self.children_movie = Movie(title="Children's Adventure", year=2020, genre=["Children"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        self.assertEqual("Classic Film (1995)", self.regular_movie.get_title())

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
