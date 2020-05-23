#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 10.
#=======================================================================

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
problem1()
#problem2()

#=======================================================================
