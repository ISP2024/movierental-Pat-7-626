from abc import ABC, abstractmethod


class PriceStrategy(ABC):
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
