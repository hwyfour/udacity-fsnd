#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser


 # class video as a parent, has title, children of movie and tv show

class Movie():
    """ This class stores movie information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self,
            movie_title,
            movie_storyline,
            movie_poster_image_url,
            movie_trailer_youtube_url):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
