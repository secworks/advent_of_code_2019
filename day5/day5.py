#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 5.
# Based on day2.
#=======================================================================

reset_state = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,6,23,27,1,5,27,31,2,31,9,35,1,35,5,39,1,39,5,43,1,43,10,47,2,6,47,51,1,51,5,55,2,55,6,59,1,5,59,63,2,63,6,67,1,5,67,71,1,71,6,75,2,75,10,79,1,79,5,83,2,83,6,87,1,87,5,91,2,9,91,95,1,95,6,99,2,9,99,103,2,9,103,107,1,5,107,111,1,111,5,115,1,115,13,119,1,13,119,123,2,6,123,127,1,5,127,131,1,9,131,135,1,135,9,139,2,139,6,143,1,143,5,147,2,147,6,151,1,5,151,155,2,6,155,159,1,159,2,163,1,9,163,0,99,2,0,14,0]

DEBUG = True

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def cpu(state):
    # Opcodes
    OP_ADD  = 1
    OP_MUL  = 2
    OP_IN   = 3
    OP_OUT  = 4
    OP_HALT = 99

    ip = 0
    done = False

    while not done:
        instr = state[ip]
        op = instr % 100
        modea = int(instr / 100) & 0x01
        modeb = int(instr / 1000)  & 0x01
        modec = int(instr / 10000) & 0x01

        if DEBUG:
            print("ip = %d, instr = %d" % (ip, instr))
            print("op = %d, modea = %d, modeb = %d, modec = %d" % (op, modea, modeb, modec))

        if op == OP_ADD:
            if DEBUG:
                print("OP_ADD")
            if modea:
                opa = state[ip + 1]
            else:
                opa = state[state[ip + 1]]

            if modeb:
                opb = state[ip + 2]
            else:
                opb = state[state[ip + 2]]

            dst = state[ip + 3]
            state[dst] = opa + opb
            ip += 4


        if op == OP_MUL:
            if DEBUG:
                print("OP_MUL")
            if modea:
                opa = state[ip + 1]
            else:
                opa = state[state[ip + 1]]

            if modeb:
                opb = state[ip + 2]
            else:
                opb = state[state[ip + 2]]

            dst = state[ip + 3]
            state[dst] = opa * opb
            ip += 4


        if op == OP_IN:
            if DEBUG:
                print("OP_IN")
            i = int(input("Input: "))
            dst = state[ip + 1]
            state[dst] = i
            ip += 2


        if op == OP_OUT:
            if DEBUG:
                print("OP_OUT")
            opa = state[ip + 1]
            dst = state[opa]
            print("Output: %d" % (dst))
            ip += 2


        if op == OP_HALT:
            if DEBUG:
                print("OP_HALT")
            done = True

    return state


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def run_prog(prog):
    state = reset_state[:]
    for i in range(len(prog)):
        state[i] = int(prog[i])
    return cpu(prog)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")

    test1_1 = [3,0,4,0,99]
    test1_2 = [1002,4,3,4,33]

#    print("Running test1_1")
#    res_state = run_prog(test1_1)
#    print("test1_1 done.")
#    print("")

    print("Running test1_2")
    res_state = run_prog(test1_2)
    print("test1_2 done.")
    print("")
    print(res_state)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
