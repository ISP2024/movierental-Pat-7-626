import logging
from price_strategy import PriceStrategy


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, price_strategy: PriceStrategy):
        # Initialize a new movie. 
        self.title = title
        self.price_strategy = price_strategy

    def get_title(self):
        return self.title

    def get_price_strategy(self):
        return self.price_strategy

    def get_rental_points(self, days):
        """Calculate the frequent renter points for a movie by days."""
        return self.get_price_strategy().get_rental_points(days)

    def get_price(self, days):
        """Calculate the price of a movie by days."""
        return self.get_price_strategy().get_price(days)
    
    def __str__(self):
        return self.title
