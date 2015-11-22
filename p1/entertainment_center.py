#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sys

import media
import fresh_tomatoes


def main(list):

    movies = []

    with open(list, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            movies.append(media.Movie(*row))

    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":

    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print 'Usage: %s <csv with movie details>' % sys.argv[0]
