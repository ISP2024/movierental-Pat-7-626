import unittest
from customer import Customer
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
        p = RegularPrice()
        m = Movie("Air", p)
        self.assertEqual("Air", m.get_title())
        self.assertEqual(p, m.get_price_strategy())

    def test_get_price(self):
        """Test to check whether get_price works correctly."""
        m = Movie("Air", RegularPrice())
        rental = Rental(m, 3)
        self.assertEqual(rental.get_price(), 3.5)

    def test_rental_points(self):
        """Test to check whether rental_points works correctly."""
        m = Movie("Air", RegularPrice())
        rental = Rental(m, 2)  # 2 days rented
        self.assertEqual(rental.get_rental_points(),
                         1)  # Regular movie earns 1 point

    @unittest.skip("add this test when you refactor rental price")
    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        self.fail("TODO add more tests for other movie categories")

    @unittest.skip("add this test of rental points when you add it to Rental")
    def test_rental_points(self):
        self.fail("add this test of frequent renter points")
