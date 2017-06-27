import settings
from entertainment_center import MovieAPI
from fresh_tomatoes import *


def main():
    print 'Fetching movies to serve...'
    mapi = MovieAPI(settings.API_KEY)
    movies = mapi.get_movies()
    open_movies_page(movies)


if __name__ == '__main__':
    main()
