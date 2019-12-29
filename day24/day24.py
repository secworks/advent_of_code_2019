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
    for i in range(len(state)):
        if state[i] == "#":
            r += 2**i
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
    new_state = get_empty_state(width, height)

    for y in range(1, (height + 1)):
        for x in range(1, (width + 1)):
            cnt = get_popcount(ms, x, y)

            if (ms[y][x] == "#") and (cnt == 1):
                new_state[(y - 1)][(x - 1)] = "#"
            else:
                new_state[(y - 1)][(x - 1)] = "."

            if (ms[y][x] == ".") and (1 <= cnt <= 2):
                new_state[(y - 1)][(x - 1)] = "#"
            else:
                new_state[(y - 1)][(x - 1)] = "."
    return new_state


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def find_loop(state):
    width = 5
    seen = set()
    while True:
        state = update_state(state, width)
        sv = calc_bio_rating(state)
        if sv not in seen:
            seen.add(sv)
        else:
            return sv


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_empty_state(width, height):
    return [["."] * width] * height


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

    print_state(test_input)
    new_state = update_state(test_input)
    print_state(new_state)

#    print_state(get_empty_state(6, 6))
#    print_state(map_state_in_state(test_input))
#    print_state(extract_state_in_state(map_state_in_state(test_input)))
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
