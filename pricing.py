from abc import ABC, abstractmethod
from datetime import datetime
from movie import Movie


class PriceStrategy(ABC):
    """Strategy class for price."""
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(PriceStrategy, cls).__new__(cls, *args,
                                                                    **kwargs)
        return cls._instances[cls]

    @abstractmethod
    def get_price(self, days):
        pass

    @abstractmethod
    def get_rental_points(self, days):
        pass


class RegularPrice(PriceStrategy):
    def get_price(self, days):
        """Two days for $2, additional days 1.50 per day."""
        if days > 2:
            return 2.0 + (1.5*(days-2))
        return 2.0

    def get_rental_points(self, days):
        """Returns 1"""
        return 1


class ChildrenPrice(PriceStrategy):
    def get_price(self, days):
        """Three days for $1.50, additional days 1.50 per day."""
        if days > 3:
            return 1.5 + (1.5*(days-3))
        return 1.5

    def get_rental_points(self, days):
        """Returns 1"""
        return 1


class NewReleasePrice(PriceStrategy):
    def get_price(self, days):
        """Straight $3 per day charge"""
        return 3 * days

    def get_rental_points(self, days):
        """Returns days"""
        return days


def get_price_code_for_movie(movie: Movie):
    """Determine the price code for a given movie."""
    current_year = datetime.now().year
    if movie.year == current_year:
        return NewReleasePrice()
    elif "Children" in movie.genre or "Childrens" in movie.genre:
        return ChildrenPrice()
    return RegularPrice()
