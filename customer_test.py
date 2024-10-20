import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie
from pricing import *


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.new_movie1 = Movie("Mulan1", NewReleasePrice())
        self.regular_movie1 = Movie("CitizenFour1", RegularPrice())
        self.children_movie1 = Movie("Frozen1", ChildrenPrice())

        self.new_movie2 = Movie("Mulan2", NewReleasePrice())
        self.regular_movie2 = Movie("CitizenFour2", RegularPrice())
        self.children_movie2 = Movie("Frozen2", ChildrenPrice())

        self.r1 = Rental(self.new_movie2, 3)
        self.r2 = Rental(self.regular_movie2, 4)
        self.r3 = Rental(self.children_movie2, 2)

        self.c1 = Customer("Movie Mogul")
        self.c2 = Customer("John Doe")

        self.c2.add_rental(self.r1)
        self.c2.add_rental(self.r2)
        self.c2.add_rental(self.r3)

    @unittest.skip("No convenient way to test")
    def test_billing(self):
        # no convenient way to test billing since its buried in the statement() method.
        pass

    def test_get_total_amount(self):
        """Test to check whether get_total_amount works correctly."""
        # Compute the expected total amount
        expected_total = self.r1.get_price() + self.r2.get_price() + self.r3.get_price()
        # Assert that the total amount is correct
        self.assertEqual(self.c2.get_total_charge(), expected_total)

    def test_get_total_rental_points(self):
        """Test to check whether get_total_rental_points works correctly."""
        # Compute the expected total rental points
        expected_total = self.r1.get_rental_points() + self.r2.get_rental_points() + self.r3.get_rental_points()
        # Assert that the total amount is correct
        self.assertEqual(self.c2.get_total_rental_points(), expected_total)

    def test_statement(self):
        stmt = self.c1.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c1.add_rental(Rental(self.new_movie1, 4))  # days
        stmt = self.c1.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
