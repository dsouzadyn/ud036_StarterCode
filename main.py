import settings
from entertainment_center import MovieAPI
from fresh_tomatoes import *


def main():
    print 'Fetching movies to serve...'
    mapi = MovieAPI(settings.API_KEY)
    movies = mapi.get_movies()
    if movies != None:
        open_movies_page(movies)
    else:
        print 'Something went wrong with the API.'


if __name__ == '__main__':
    main()
