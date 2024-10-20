import unittest
from pricing import *


class TestPriceCodeForMovie(unittest.TestCase):
    """Tests of get_price_code_for_movie"""

    def test_new_release_movie(self):
        """Test NewReleasePrice movie."""
        movie = Movie(title="Latest Blockbuster", year=datetime.now().year, genre=["Action"])
        price_code = get_price_code_for_movie(movie)
        self.assertIsInstance(price_code, NewReleasePrice)

    def test_children_movie(self):
        """Test ChildrenPrice movie."""
        movie = Movie(title="Children's Adventure", year=2020, genre=["Children"])
        price_code = get_price_code_for_movie(movie)
        self.assertIsInstance(price_code, ChildrenPrice)

    def test_regular_movie(self):
        """Test RegularPrice movie."""
        movie = Movie(title="Classic Film", year=1995, genre=["Drama"])
        price_code = get_price_code_for_movie(movie)
        self.assertIsInstance(price_code, RegularPrice)
