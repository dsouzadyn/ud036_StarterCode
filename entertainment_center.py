import requests
import media


class MovieAPI:
        # This is the Movie API class, built to handle all the
        # functionality of acquiring movies using themoviedb api.

    def __init__(self, API_KEY=''):
        self.API_KEY = API_KEY

    def get_movies(self):
        # Outputs a list of popular movies from themoviedb.org.
        movies = []
        movie_endpoint = 'https://api.themoviedb.org/3/discover/movie?api_key={0}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'.format(
            self.API_KEY)
        response = requests.request("GET", movie_endpoint)
        data = response.json()
        results = data['results']
        for movie in results:
            m = media.Movie()
            m.set_title(movie['original_title'])
            m.set_trailer_url(self.get_video(movie['id']))
            m.set_poster_url(
                'https://image.tmdb.org/t/p/w640{}'.format(movie['poster_path']))
            movies.append(m)
        return movies

    def get_video(self, movie_id):
        # This function takes the movie_id(string) and returns the youtube trailer url.
        # If no trailer url is found, then an empty string is returned.
        video_endpoint = 'https://api.themoviedb.org/3/movie/{0}/videos?api_key={1}&language=en-US'.format(
            movie_id, self.API_KEY)
        response = requests.request("GET", video_endpoint)
        data = response.json()
        results = data['results']
        if len(results) > 0:
            return 'http://www.youtube.com/watch?v={0}'.format(results[0]['key'])
        else:
            return ''
