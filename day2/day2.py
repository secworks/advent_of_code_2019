#!/usr/bin/env python3

# Solutions to Advent of Code 2019, day 2.


reset_state = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,6,23,27,1,5,27,31,2,31,9,35,1,35,5,39,1,39,5,43,1,43,10,47,2,6,47,51,1,51,5,55,2,55,6,59,1,5,59,63,2,63,6,67,1,5,67,71,1,71,6,75,2,75,10,79,1,79,5,83,2,83,6,87,1,87,5,91,2,9,91,95,1,95,6,99,2,9,99,103,2,9,103,107,1,5,107,111,1,111,5,115,1,115,13,119,1,13,119,123,2,6,123,127,1,5,127,131,1,9,131,135,1,135,9,139,2,139,6,143,1,143,5,147,2,147,6,151,1,5,151,155,2,6,155,159,1,159,2,163,1,9,163,0,99,2,0,14,0]


def run_prog(noun, verb):
    prog = reset_state[:]
    prog[1] = noun
    prog[2] = verb
    return cpu(prog)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def cpu(state):
    ip = 0

    while state[ip] != 99:
        op  = state[ip]
        opa = state[state[ip + 1]]
        opb = state[state[ip + 2]]
        dst = state[ip + 3]

        if op == 1:
            state[dst] = opa + opb

        if op == 2:
            state[dst] = opa * opb
        ip += 4
    return state


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    tests1 = [([1,0,0,0,99], [2,0,0,0,99]),
              ([2,3,0,3,99], [2,3,0,6,99]),
              ([2,4,4,5,99,0], [2,4,4,5,99,9801]),
              ([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])]

    for state, exp in tests1:
        print("Got: ", cpu(state), "expected: ", exp)

    print("Running the real program")
    res = run_prog(12, 2)
    print("state[0] after execution: %d" % res[0])

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    for noun in range(50):
        for verb in range(50):
            res = run_prog(noun, verb)
            if res[0] == 19690720:
                print("Founded it! noun: %d, verb: %d" % (noun, verb))
                print("Answer: %d" % (100 * noun + verb))
#            print("res[0] for noun %d and verb %d: %d" % (noun, verb, res[0]))


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()
