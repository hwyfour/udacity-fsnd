#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sys

import media
import fresh_tomatoes


'''
This function loads a CSV of movie details and calls the fresh_tomatoes code to generate
a static HTML page containing the details of each movie within the CSV. For each row in the
file, initialize a new Movie object with the details contained within the row.
'''
def main(list):

    # initialize an array to store our movie details
    movies = []

    # open the provided CSV as the iterable CSV object 'reader'
    with open(list, 'rb') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            '''
            Using the asterisk transparently unpacks the row object into its constituent parts
            which are then sent to the Movie object as individual arguments. This is useful as a
            clean shortcut to initilize a Movie object, provided the CSV follows the schema.
            '''
            movies.append(media.Movie(*row))

    # open the newly generated page containing our movie information!
    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":

    # only enter the program iff there are 2 arguments
    if len(sys.argv) == 2:
        # run the main function to populate the movie data!
        main(sys.argv[1])
    else:
        print 'Usage: %s <csv with movie details>' % sys.argv[0]
