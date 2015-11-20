#!/usr/bin/env python
# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story",
    "A story about toys",
    "http://ia.media-imdb.com/images/M/MV5BMTYzNzU5MzQ4OV5BMl5BanBnXkFtZTcwMDcxNDg3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",
    "https://www.youtube.com/watch?v=XKSQmYUaIyE")

movies = [toy_story]

fresh_tomatoes.open_movies_page(movies)
