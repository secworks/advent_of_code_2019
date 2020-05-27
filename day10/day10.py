#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 10.
#=======================================================================

DEBUG = True

from math import gcd

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open("day10_input.txt",'r') as f:
        for line in f:
            l.append(line.strip())
    return l


#-------------------------------------------------------------------
# Find coodinates for all asteroids. Not sure if this is needed.
#-------------------------------------------------------------------
def find_all_asteroids(board):
    columns = len(board)
    rows = len(board[0])
    print("Field width and height: (%d, %d)" % (columns, rows))
    print("Total positions: %d" % (columns * rows))
    print("")

    asteroids = []
    for r in range(rows):
        curr_row = board[r]
        for c in range(columns):
            if curr_row[c] == "#":
                asteroids.append((c, r))
                print("Asteroid at (%d, %d)" % (c, r))
    return asteroids


#-------------------------------------------------------------------
# Generate the list of edgepoints for an area.
#-------------------------------------------------------------------
def get_edgepoints(dimx, dimy):
    edgepoints = []

    edgepoints.extend([(0, y) for y in range(dimy)])
    edgepoints.extend([((dimx - 1), y) for y in range(dimy)])

    edgepoints.extend([(x, 0) for x in range(dimx)])
    edgepoints.extend([(x, (dimy - 1)) for x in range(dimx)])

    return edgepoints


#-------------------------------------------------------------------
# Generate a list of all coordinates to check between the
# start coordinate (x0, y0) and the end coordinate (x0. y0).
# The coordinates are order by distance to the start coordinate.
#-------------------------------------------------------------------
def get_coords(x0, y0, x1, y1):
    if DEBUG:
        print("get_coords: (%d, %d) -> (%d, %d)" % (x0, y0, x1, y1))

    # Check if we are trying to draw to the same point.
    if (x0 == x1) and (y0 == y1):
        return []

    points = gcd(abs(x1 - x0), abs(y1 - y0))
    dx = (x1 - x0) / points
    dy = (y1 - y0) / points
    return [(int(x0 + r * dx), int(y0 + r * dy)) for r in range(1, (points + 1))]


#-------------------------------------------------------------------
# Given a point, get all points to check on a board.
# Note that the points returned are ordered as a list of lists.
# Each list contains zero, one or more points. The points
# in a given list should be evaluated in order.
#-------------------------------------------------------------------
def get_points_for_point(x0, y0, dimx, dimy):
    edgepoints = get_edgepoints(dimx, dimy)
    my_points = []
    for point in edgepoints:
        (x1, y1) = point
        my_points.append(get_coords(x0, y0, x1, y1))
    return my_points


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def test_points_for_points():
    my_points = get_points_for_point(1, 2, 4, 4)
    for line in my_points:
        for point in line:
            print(point)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def test_get_edgepoints():
    print(get_edgepoints(2, 2))
    print(get_edgepoints(5, 5))


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def test_get_coords():
    print(get_coords(1, 1, 1, 4))
    print("")
    print(get_coords(1, 4, 1, 1))
    print("")

    print(get_coords(3, 3, 12, 3))
    print("")
    print(get_coords(12, 3, 3, 3))
    print("")

    print(get_coords(1, 9, 8, 16))
    print("")
    print(get_coords(8, 16, 1, 9))
    print("")
    print(get_coords(0, 0, 4, 16))
    print("")
    print(get_coords(0, 0, 0, 0))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")

    my_map = get_input("day10_input.txt")
    print("My map:")
    print(my_map)
    print("")

    my_asteroids = find_all_asteroids(my_map)
    print("Total number of asteroids: %d" % (len(my_asteroids)))
    print("My asteroids are at:")
    print(my_asteroids)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
#test_get_coords()
#test_get_edgepoints()
test_points_for_points()

#problem1()
#problem2()

#=======================================================================
