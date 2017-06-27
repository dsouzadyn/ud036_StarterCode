class Movie:

    def __init__(self):
        self.title = ''
        self.trailer_youtube_url = ''
        self.poster_image_url = ''

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_trailer_url(self, url):
        self.trailer_youtube_url = url

    def get_trailer_url(self):
        return self.trailer_youtube_url

    def set_poster_url(self, url):
        self.poster_image_url = url

    def get_poster_url(self):
        return self.poster_image_url
