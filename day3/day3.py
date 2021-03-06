#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 3.
#=======================================================================

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(line.strip())
    return l


#-------------------------------------------------------------------
# Return a list of line segments by traversing a given wire.
#-------------------------------------------------------------------
def get_segments(wire):
    segments = []
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    for segment in wire:
        direction = segment[0]
        distance = int(segment[1:])

        if direction == "L":
            x1 = x0 - distance
            segments.append(("H", (x0, y0), (x1, y1)))

        if direction == "R":
            x1 = x0 + distance
            segments.append(("H", (x0, y0), (x1, y1)))

        if direction == "U":
            y1 = y0 - distance
            segments.append(("V", (x0, y0), (x1, y1)))

        if direction == "D":
            y1 = y0 + distance
            segments.append(("V", (x0, y0), (x1, y1)))

        x0 = x1
        y0 = y1

    return segments


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def wires_crossed(sega, segb):
    (adir, ap0, ap1) = sega
    ax0, ay0 = ap0
    ax1, ay1 = ap1

    (bdir, bp0, bp1) = segb
    bx0, by0 = bp0
    bx1, by1 = bp1

    if adir == bdir:
        return False
    else:
        if adir == "H":
            if ((ax0 <= bx0 <= ax1) or (ax1 <= bx0 <= ax0)):
                if ((by0 <= ay0 <= by1) or (by1 <= ay0 <= by0)):
                    return True
        else:
            if ((bx0 <= ax0 <= bx1) or (bx1 <= ax0 <= bx0)):
                if ((ay0 <= by0 <= ay1) or (ay1 <= by0 <= ay0)):
                    return True
    return False


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_point(sega, segb):
    (adir, ap0, ap1) = sega
    ax0, ay0 = ap0
    ax1, ay1 = ap1

    (bdir, bp0, bp1) = segb
    bx0, by0 = bp0
    bx1, by1 = bp1

    if adir == "H":
        return (bx0, ay0)
    else:
        return (ax0, by0)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_min_manhattan(points):
    min_manhattan = 10000000
    for (x, y) in points:
        distance = abs(x) + abs(y)
        if  distance < min_manhattan:
            min_manhattan = distance
    return min_manhattan


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_crosses(wires):
    wire0 = get_segments(wires[0].split(','))
    wire1 = get_segments(wires[1].split(','))

    crosses = []
    for segment0 in wire0:
        for segment1 in wire1:
            if wires_crossed(segment0, segment1):
                point = get_point(segment0, segment1)
                if point != (0, 0):
                    crosses.append(point)
    return crosses


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_wlen(cross, wire):
    cx, cy = cross

    wlen = 0
    for w in wire:
        (d, p0, p1) = w
        (x0, y0) = p0
        (x1, y1) = p1

        if d == "H":
            if ((x0 <= cx <= x1) or (x1 <= cx <= x0)) and (cy == y0):
                if x0 >= cx:
                    wlen += abs(x0 - cx)
                else:
                    wlen += abs(cx - x0)
                return wlen
            else:
                wlen += abs(x0 - x1)

        if d == "V":
            if ((y0 <= cy <= y1) or (y1 <= cy <= y0)) and (cx == x0):
                if y0 >= cy:
                    wlen += abs(y0 - cy)
                else:
                    wlen += abs(cy - y0)
                return wlen
            else:
                wlen += abs(y1 - y0)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")

#   my_wires = get_input("day3_testinput1.txt")
#   my_wires = get_input("day3_testinput2.txt")

    my_wires = get_input("day3_input1.txt")
    my_crosses = get_crosses(my_wires)
    print(get_min_manhattan(my_crosses))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")

#    my_wires = get_input("day3_testinput1.txt")
#    my_wires = get_input("day3_testinput2.txt")
    my_wires = get_input("day3_input1.txt")

    my_crosses = get_crosses(my_wires)
    wire0 = get_segments(my_wires[0].split(','))
    wire1 = get_segments(my_wires[1].split(','))

    min_len = 100000
    for cross in my_crosses:
        wlen0 = get_wlen(cross, wire0)
        wlen1 = get_wlen(cross, wire1)

        tot_len = wlen0 + wlen1
        if (tot_len < min_len):
            min_len = tot_len
            min_cross = cross

    print("Min total wire length: %d" % min_len)
    print("Cross with min len:   ", min_cross)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()
#=======================================================================
