class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title):
        self.title = title

    def get_title(self):
        """Get the title of the movie."""
        return self.title

    def __str__(self):
        return self.title
