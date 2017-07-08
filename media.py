# This Class provides the python data structure used to store
# the attributes for the movie objects.
import webbrowser

class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Initialises an instance object of the movie class
        with the data provided with the parameters.
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens the default webbrowser and displays the trailer of
        the movie object.
        """
        webbrowser.open(self.trailer_youtube_url)
