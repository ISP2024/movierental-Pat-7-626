import logging
from pricing import PriceStrategy


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, price_strategy: PriceStrategy):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_strategy

    def get_title(self):
        return self.title

    def get_price_code(self):
        return self.price_code

    def __str__(self):
        return self.title
