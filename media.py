class Video:
    """Base class for videos.
    """

    def __init__(self, video_title, video_trailer):
        """The Video class constructor takes 2 arguments.
        Args:
            movie_title (str): The title of the video
            movie_trailer (str): Link of the video
        """
        self.title = video_title
        self.trailer_youtube_url = video_trailer

    def set_title(self, title):
        """This class method takes a single argument.
        Args:
            title: The title of the video
        Returns:
            Nothing
        """
        self.title = title

    def get_title(self):
        """This class method returns the title of a given Video instance.
        Returns:
            title (str): Title of the video
        """
        return self.title

    def set_trailer_url(self, url):
        """This class method is used to set the video link.
        Args:
            url (str): Video link
        Returns:
            Nothing
        """
        self.trailer_youtube_url = url

    def get_trailer_url(self):
        """This class method returns the video link of a given Video instance.
        Returns:
            trailer_url (str): Link of the video
        """
        return self.trailer_youtube_url


class Movie(Video):
    """The Movie class used to represent movies as objects.
    This class inherits from the Video class
    """

    def __init__(self, movie_title, movie_trailer, movie_poster):
        """The Movie constructor takes 3 arguments.
        Args:
            movie_title (str): Title of the movie
            movie_trailer (str): Link of the movie trailer
            movie_poster (str): Link of the movie poster
        """
        Video.__init__(self, movie_title, movie_trailer)
        self.poster_image_url = movie_poster

    def set_poster_url(self, url):
        """This class method is used to set the link of the movie poster
        Args:
            url (str): Link of movie poster
        Returns:
            Nothing
        """
        self.poster_image_url = url

    def get_poster_url(self):
        """Used to get the link of the movie poster
        Returns:
            url (str): Link of movie poster
        """
        return self.poster_image_url
