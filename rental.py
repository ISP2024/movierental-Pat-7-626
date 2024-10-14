import logging
from movie import Movie


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
        a movie with known rental period (daysRented)."""
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        """Calculate the price of a rental."""
        amount = 0
        price_code = self.get_movie().get_price_code()
        days_rented = self.get_days_rented()

        if price_code == Movie.REGULAR:
            # Two days for $2, additional days 1.50 per day.
            amount = 2.0
            if days_rented > 2:
                amount += 1.5 * (days_rented - 2)
        elif price_code == Movie.CHILDRENS:
            # Three days for $1.50, additional days 1.50 per day.
            amount = 1.5
            if days_rented > 3:
                amount += 1.5 * (days_rented - 3)
        elif price_code == Movie.NEW_RELEASE:
            # Straight $3 per day charge
            amount = 3 * days_rented
        else:
            log = logging.getLogger()
            log.error(
                f"Movie {self.get_movie()} has unrecognized priceCode {price_code}")

        return amount

    def rental_points(self):
        """Calculate the frequent renter points for a rental."""
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            # New release earns 1 point per day rented
            return self.get_days_rented()
        return 1

    def get_rental_points(self):
        """Calculate rental points based on the rental type."""
        return self.rental_points()
