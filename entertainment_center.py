import requests
import media


class MovieAPI:
    """This class is built to make interaction with themoviedb.org's API easy.
    """

    def __init__(self, API_KEY=''):
        """The MovieAPI constructor takes 1 argument.
        Args:
            API_KEY (str): themoviedb.org API key
        """
        self.API_KEY = API_KEY

    def get_movies(self):
        """This class method queries themoviedb.org's API and returns a list of 20
        most poular Movie items.
        Returns:
            List of Movie objects.
        """
        movies = []
        if self.API_KEY != '':
            movie_endpoint = 'https://api.themoviedb.org/3/discover/movie?api_key={0}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'.format(
                self.API_KEY)
            response = requests.request("GET", movie_endpoint)
            data = response.json()
            results = data['results']
            for movie in results:
                movie_title = movie['original_title']
                movie_trailer = self.get_video(movie['id'])
                movie_poster = 'https://image.tmdb.org/t/p/w640{}'.format(movie[
                                                                          'poster_path'])
                if movie_trailer != None:
                    print 'Preparing movie: {0}'.format(movie_title)
                    m = media.Movie(movie_title, movie_trailer, movie_poster)
                    movies.append(m)
                else:
                    print 'Skipping movie: {0}. Reason: No trailer found.'.format(movie_title)
        else:
            print 'Did you specify the API key?'
            return None
        return movies

    def get_video(self, movie_id):
        """This class method queries themovidb.org's API and get's the trailer link.
        Args:
            movie_id (str): The id of the movie whose trailer url is required
        Returns:
            A string of the trailer url if successful. Else it returns a blank string.
        """
        if self.API_KEY != '':
            video_endpoint = 'https://api.themoviedb.org/3/movie/{0}/videos?api_key={1}&language=en-US'.format(
                movie_id, self.API_KEY)
            response = requests.request("GET", video_endpoint)
            data = response.json()
            results = data['results']
            if len(results) > 0:
                return 'http://www.youtube.com/watch?v={0}'.format(results[0]['key'])
            else:
                return ''
        else:
            print 'Did you specify the API key?'
            return None
