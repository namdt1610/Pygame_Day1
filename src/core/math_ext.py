from math import sqrt


def distance(x, y, other_x, other_y):
    return sqrt((x - other_x) ** 2 + (y - other_y) ** 2) ** 0.5
