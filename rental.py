from pricing import PriceStrategy


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie, days_rented, price_code: PriceStrategy):
        """Initialize a new movie rental object for
        a movie with known rental period (daysRented)."""
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    def get_movie(self):
        """Get the movie for this rental."""
        return self.movie

    def get_days_rented(self):
        """Get the days rented for this rental."""
        return self.days_rented

    def get_price_code(self):
        """Get the price code for this rental."""
        return self.price_code

    def get_price(self):
        """Calculate the price of a rental."""
        return self.get_price_code().get_price(self.get_days_rented())

    def get_rental_points(self):
        """Calculate the frequent renter points for a rental."""
        return self.get_price_code().get_rental_points(self.get_days_rented())
