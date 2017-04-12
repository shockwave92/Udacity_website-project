import webbrowser

class Movie():
    """
    This class provides a way to store movie related information
    """
    
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = youtube_trailer
        self.release = release_date
