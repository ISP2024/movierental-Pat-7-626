from dataclasses import dataclass
from typing import Optional, List
import csv


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """

    title: str
    year: int
    genre: List[str]

    def is_genre(self, genre_name):
        """Check if the movie belongs to a given genre."""
        return genre_name.lower() in (g.lower() for g in self.genre)

    def get_title(self):
        """Get the title of the movie."""
        return f"{self.title} ({self.year})"

    def __str__(self):
        return self.title


class MovieCatalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance.movies = []
            cls._instance.load_movies_from_file("movies.csv")
        return cls._instance

    def load_movies_from_file(self, file_path: str):
        """
        Load movies from a CSV file, processing one line at a time.
        Each line is converted into a Movie object.
        """
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row["Title"]
                year = int(row["Year"])
                genres = row["Genres"].split(",")
                movie = Movie(title=title, year=year, genre=genres)
                self.movies.append(movie)

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        """
        Get a movie by title and optional year. If year is omitted, return the first matching movie.
        """
        for movie in self.movies:
            if (movie.title.lower() == title.lower()
                    and (year is None or movie.year == year)):
                return movie
        return None
