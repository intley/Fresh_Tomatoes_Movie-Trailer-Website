# This file consists of the various instances of the movie class
# contained inside the file media.py
# These instance objects are retrieved using the TMDB API
import json
import requests
import media
import fresh_tomatoes

# Registered API Key used to access TMDB library. CONFIDENTIAL!
api_key = "e400eed6be0d79125ca4eef688fe671d"

def api_query(movie_id):
    """This function forms the standard query to get the details of a movie
    with the movie id
    """
    url_response = ("https://api.themoviedb.org/3/movie/" + movie_id +
                    "?api_key=" + api_key + "&append_to_response=videos")
    response = requests.get(url_response)
    json_response = response.json()
    return json_response

def api_title(res):
    """Returns the movie title which is retrieved from the JSON object
    of the api_query method which contains the movie details.
    """
    movie_title = res["original_title"]
    return movie_title

def api_poster(res):
    """Returns the poster which is retrieved from the JSON object
    of the api_query method which contains the movie details.
    """
    json_poster = res["poster_path"]
    poster_image = "https://image.tmdb.org/t/p/w500" + json_poster
    return poster_image

def api_trailer(res, index):
    """Returns the trailer link after parsing and retrieved using the key
    attribute from the JSON object of the api_query method.
    """
    json_video = res["videos"]["results"][index]
    trailer_url = json_video["key"]
    trailer_video = "https://www.youtube.com/watch?v=" + str(trailer_url)
    return trailer_video

# Instance Object 1: The Dark Knight
batman_id = "155"
batman_title = api_title(api_query(batman_id))
batman_poster = api_poster(api_query(batman_id))
batman_trailer = api_trailer(api_query(batman_id), 0)
batman = media.Movie(batman_title, batman_poster, batman_trailer)

# Instance Object 2: Forrest Gump
forrest_gump_id = "13"
forrest_gump_title = api_title(api_query(forrest_gump_id))
forrest_gump_poster = api_poster(api_query(forrest_gump_id))
forrest_gump_trailer = api_trailer(api_query(forrest_gump_id), 0)
forrest_gump = media.Movie(forrest_gump_title, forrest_gump_poster,
                           forrest_gump_trailer)

# Instance Object 3: The Big Sick
big_sick_id = "416477"
big_sick_title = api_title(api_query(big_sick_id))
big_sick_poster = api_poster(api_query(big_sick_id))
big_sick_trailer = api_trailer(api_query(big_sick_id), 0)
big_sick = media.Movie(big_sick_title, big_sick_poster, big_sick_trailer)

# Instance Object 4: 50/50
fifty_fifty_id = "40807"
fifty_fifty_title = api_title(api_query(fifty_fifty_id))
fifty_fifty_poster = api_poster(api_query(fifty_fifty_id))
fifty_fifty_trailer = api_trailer(api_query(fifty_fifty_id), 0)
fifty_fifty = media.Movie(fifty_fifty_title, fifty_fifty_poster,
                          fifty_fifty_trailer)

# Instance Object 5: Good Will Hunting
good_will_id = "489"
good_will_title = api_title(api_query(good_will_id))
good_will_poster = api_poster(api_query(good_will_id))
good_will_trailer = api_trailer(api_query(good_will_id), 0)
good_will = media.Movie(good_will_title, good_will_poster, good_will_trailer)

# Instance Object 6: The Godfather
godfather_id = "238"
godfather_title = api_title(api_query(godfather_id))
godfather_poster = api_poster(api_query(godfather_id))
godfather_trailer = api_trailer(api_query(godfather_id), 0)
godfather = media.Movie(godfather_title, godfather_poster, godfather_trailer)

# Using the fresh tomatoes file, a html page is generated with the list of
# movie objects
movies = [batman, forrest_gump, big_sick, fifty_fifty, good_will, godfather]
fresh_tomatoes.open_movies_page(movies)
