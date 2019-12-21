#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 16.
#=======================================================================

import math

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    indata = []
    with open(filename,'r') as f:
        line = f.read()
    return [int(x) for x in line.strip()]


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def calc_phase(e, pattern):
    o = [0] * len(e)

    my_ptrs = dict()
    # Build db with metadata tuples.
    for i in range(len(e)):
        pattern_ptr = 0
        reps = i + 1
        reps_ctr = 0
        my_ptrs[i] = (pattern_ptr, reps, reps_ctr)

    for i in range(len(e)):
        (pattern_ptr, reps, reps_ctr) = my_ptrs[i]
        acc = 0
        for j in range(len(e)):
            reps_ctr += 1
            if reps_ctr == reps:
                reps_ctr = 0
                pattern_ptr += 1
                if pattern_ptr == len(pattern):
                    pattern_ptr = 0
            acc += e[j] * pattern[pattern_ptr]
        o[i] = abs(acc) % 10

    return o


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def calc_phase_n(phase, pattern, n):
    for i in range(n):
        phase = calc_phase(phase, pattern)
    return phase[:8]

def l2s(l):
    return str(l[0]) + str(l[1]) + str(l[2]) + str(l[3]) + str(l[4]) +\
           str(l[4]) + str(l[5]) + str(l[6]) + str(l[7])

#-------------------------------------------------------------------
# problem1
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    pattern = [0, 1, 0, -1]
    test_input1 = [1, 2, 3, 4, 5, 6, 7, 8]
    test_input2 = [8,0,8,7,1,2,2,4,5,8,5,9,1,4,5,4,6,6,1,9,0,8,3,2,1,8,6,4,5,5,9,5]
    test_input3 = [1,9,6,1,7,8,0,4,2,0,7,2,0,2,2,0,9,1,4,4,9,1,6,0,4,4,1,8,9,9,1,7]
    test_input4 = [6,9,3,1,7,1,6,3,4,9,2,9,4,8,6,0,6,3,3,5,9,9,5,9,2,4,3,1,9,8,7,3]
    problem1_input = get_input("day16_input.txt")

    print("Result of test1 after 4 phase calculations:")
    print(l2s(calc_phase_n(test_input1, pattern, 4)))
    print("")

    print("Result of test2 after 100 phase calculations:")
    print(l2s(calc_phase_n(test_input2, pattern, 100)))
    print("")

    print("Result of test3 after 100 phase calculations:")
    print(l2s(calc_phase_n(test_input3, pattern, 100)))
    print("")

    print("Result of test4 after 100 phase calculations:")
    print(l2s(calc_phase_n(test_input4, pattern, 100)))
    print("")

    print("Result of problem1 input after 100 phase calculations:")
    print(l2s(calc_phase_n(problem1_input, pattern, 100)))
    print("")


#-------------------------------------------------------------------
# problem2
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    pattern = [0, 1, 0, -1]
    test_input1 = [1, 2, 3, 4, 5, 6, 7, 8] * 10000
    test_input2 = [8,0,8,7,1,2,2,4,5,8,5,9,1,4,5,4,6,6,1,9,0,8,3,2,1,8,6,4,5,5,9,5] * 10000
    test_input3 = [1,9,6,1,7,8,0,4,2,0,7,2,0,2,2,0,9,1,4,4,9,1,6,0,4,4,1,8,9,9,1,7] * 10000
    test_input4 = [6,9,3,1,7,1,6,3,4,9,2,9,4,8,6,0,6,3,3,5,9,9,5,9,2,4,3,1,9,8,7,3] * 10000
    problem1_input = get_input("day16_input.txt")
    problem1_input = problem1_input * 10000

    print("Result of test1 after 4 phase calculations:")
    print(l2s(calc_phase_n(test_input1, pattern, 4)))
    print("")

    print("Result of test2 after 100 phase calculations:")
    print(l2s(calc_phase_n(test_input2, pattern, 100)))
    print("")

    print("Result of test3 after 100 phase calculations:")
    print(l2s(calc_phase_n(test_input3, pattern, 100)))
    print("")

    print("Result of test4 after 100 phase calculations:")
    print(l2s(calc_phase_n(test_input4, pattern, 100)))
    print("")

    print("Result of problem1 input after 100 phase calculations:")
    print(l2s(calc_phase_n(problem1_input, pattern, 100)))
    print("")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
