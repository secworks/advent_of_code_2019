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
    return [(int(x0 + r * dx), int(y0 + r*dy)) for r in range(1, (points + 1))]

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
test_get_coords()

#problem1()
#problem2()

#=======================================================================
