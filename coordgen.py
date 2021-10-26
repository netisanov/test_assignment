import geopy.distance
from random import randint


def generator(latitude, longitude):
    meters = randint(1, 101)
    bearing = randint(0, 360)
    return \
        geopy.distance.distance(meters=meters).destination((latitude, longitude), bearing=bearing)



def coordnates_generator(latitude, longitude, count):
    count = count
    while count > 0:
        count -= 1
        point = generator(latitude, longitude)
        print(point.latitude, point.longitude)
        latitude = point.latitude
        longitude = point.longitude





