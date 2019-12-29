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
def is_populated(x, y, state, width, height):
    if x < 0 or x > width:
        return False
    if y < 0 or y > height:
        return False

    i = y * width + x
    print(x, y, i)

    if state[i] == "#":
        return True
    else:
        return False

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def update_state(state, width):
    height = int(len(state) / width)
    new_state = ["."] * len(state)
    done = False
    x = 0
    y = 0
    while (x < width) and (y < height):
        pop = 0
        if is_populated((x - 1), y, state, width - 1, height - 1):
            pop += 1
        if is_populated((x + 1), y, state, width - 1, height - 1):
            pop += 1
        if is_populated(x, (y - 1), state, width - 1, height - 1):
            pop += 1
        if is_populated(x, (y + 1), state, width - 1, height - 1):
            pop += 1

        i = width * y + x

        if (state[i] == "#") and (pop == 1):
            new_state[i] = "#"
        else:
            new_state[i] = "."

        if (state[i] == ".") and (1 <= pop <= 2):
            new_state[i] = "#"
        else:
            new_state[i] = "."

        x += 1
        if x == width:
            x = 0
            y += 1

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
    print_state(get_empty_state(6, 6))
    print_state(map_state_in_state(test_input))
    print_state(extract_state_in_state(map_state_in_state(test_input)))
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
