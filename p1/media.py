#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Movie():
    """ This class stores movie information """

    def __init__(self,
            movie_title,
            movie_storyline,
            movie_year,
            movie_rating,
            movie_length,
            movie_poster_image_url,
            movie_trailer_youtube_url):

        self.title = movie_title
        self.storyline = movie_storyline
        self.year = movie_year
        self.rating = movie_rating
        self.length = movie_length
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url
