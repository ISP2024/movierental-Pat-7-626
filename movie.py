from dataclasses import dataclass
from typing import Collection


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """

    title: str
    year: int
    genre: Collection[str]

    def is_genre(self, genre_name):
        """Check if the movie belongs to a given genre."""
        return genre_name.lower() in (g.lower() for g in self.genre)

    def get_title(self):
        """Get the title of the movie."""
        return f"{self.title} ({self.year})"

    def __str__(self):
        return self.title
