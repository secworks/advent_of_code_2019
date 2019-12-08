#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 8.
# Based on day5.
#=======================================================================

DEBUG = False

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    with open(filename,'r') as f:
        l = f.read()
    return l.strip()


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_planes(s):
    planes = []
    row = []
    plane = []
    for c in s:
        row.append(c)

        if len(row) == 25:
            plane.append(row)
            row = []

        if len(plane) == 6:
            planes.append(plane)
            plane = []

    return planes


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_min_zero(planes):
    i = 0
    mz = 10000
    mi = 0
    for plane in planes:
        ctr = 0
        for row in plane:
            for c in row:
                if c == '0':
                    ctr += 1
        if ctr < mz:
            mz = ctr
            mi = i
        i += 1

    print("Plane with min zeroes is %d. It contains %d zeroes" % (mi, mz))
    return mi


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_one_two(plane):
    ones = 0
    twos = 0
    for row in plane:
        for c in row:
            if c == '1':
                ones += 1
            if c == '2':
                twos += 1
    print("Number of ones: %d. Number of twos: %d" % (ones, twos))
    return ones * twos


#-------------------------------------------------------------------
# problem1
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    my_input = get_input("day8_input.txt")
    my_planes = get_planes(my_input)
    zi = get_min_zero(my_planes)
    p1_res = get_one_two(my_planes[zi])
    print("Number of ones multiplies by number of twos: %d" % p1_res)
    print("")


#-------------------------------------------------------------------
# problem2
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
