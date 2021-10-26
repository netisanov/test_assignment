import geopy.distance

from random import randint


def get_difference_btw_dates(start, end):
    delta = end - start
    difference = delta.seconds // 60
    return difference


def get_random_coordinate(latitude, longitude):
    meters = randint(1, 101)
    bearing = randint(0, 360)
    point = geopy.distance.distance(meters=meters).destination((latitude, longitude), bearing=bearing)
    return point
