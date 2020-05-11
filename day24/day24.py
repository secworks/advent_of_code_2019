#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 24.
#
# We keep the state as an arrar with rows.
# We map the array of rows into a larger array when calculating
# next state.
#=======================================================================

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    indata = []
    with open(filename,'r') as f:
        for line in f:
            indata.append(line.strip())
    return indata


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def print_state(state):
    for row in state:
        print("".join(row))
    print()


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def calc_bio_rating(state):
    r = 0
    i = 0
    for y in range(len(state)):
        for x in range(len(state[0])):
            if state[y][x] == "#":
                r += 2**i
            i += 1
    return r


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_popcount(state, x, y):
    cnt = 0
    if state[y][(x - 1)] == "#":
        cnt += 1
    if state[y][(x + 1)] == "#":
        cnt += 1
    if state[(y - 1)][x] == "#":
        cnt += 1
    if state[(y + 1)][x] == "#":
        cnt += 1
    return cnt


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def update_state(state):
    height = len(state)
    width = len(state[0])

    ms = map_state_in_state(state)
    print_state(ms)
    new_state = get_empty_state(width, height)
    print_state(new_state)

    for y in range(1, (height + 1)):
        for x in range(1, (width + 1)):
            cnt = get_popcount(ms, x, y)

            if (ms[y][x] == "#") and (cnt == 1):
                new_state[(y - 1)][(x - 1)] = "#"

            elif (ms[y][x] == "#"):
                new_state[(y - 1)][(x - 1)] = "."

            elif (ms[y][x] == ".") and (1 <= cnt <= 2):
                new_state[(y - 1)][(x - 1)] = "#"

            else:
                new_state[(y - 1)][(x - 1)] = "."
    return new_state


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def find_loop(state):
    seen = set()
    br = calc_bio_rating(state)
    seen.add(br)
    loop = False

    while not loop:
        state = update_state(state)
        br = calc_bio_rating(state)

        if br not in seen:
            seen.add(br)
        else:
            print("Found loop. Biodiversity: %d:" % br)
            print_state(state)
            loop = True

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_empty_state(width, height):
    return [["." for x in range(width)] for y in range(height)]


#-------------------------------------------------------------------
# map_state_in_state()
# Map state into 2x2 element larger state.
#-------------------------------------------------------------------
def map_state_in_state(state):
    new_state = get_empty_state((len(state[0]) + 2), (len(state) + 2))
    y = 1
    for row in state:
        new_state[y] = ["."] + row + ["."]
        y += 1
    return new_state


#-------------------------------------------------------------------
# extraxt_state_from_state()
# Extract state from 2x2 element larger state.
#-------------------------------------------------------------------
def extract_state_in_state(state):
    state.pop(0)
    state.pop((len(state) - 1))
    new_state = []
    for row in state:
        new_state.append(row[1:-1])
    return new_state


#-------------------------------------------------------------------
# problem1
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    my_input = [["#", ".", "#", ".", "."],
                [".", "#", "#", "#", "."],
                [".", ".", ".", "#", "."],
                ["#", "#", "#", ".", "."],
                ["#", ".", ".", ".", "."]]

    test_input = [[".", ".", ".", ".", "#"],
                  ["#", ".", ".", "#", "."],
                  ["#", ".", ".", "#", "#"],
                  [".", ".", "#", ".", "."],
                  ["#", ".", ".", ".", "."]]

    find_loop(my_input)
    print("")




#-------------------------------------------------------------------
# problem2
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
