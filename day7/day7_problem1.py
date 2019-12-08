#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 7.
# Based on day5.
#=======================================================================

DEBUG = False

import itertools


puzzle_prog = [3,8,1001,8,10,8,105,1,0,0,21,46,59,84,93,110,191,272,353,434,99999,3,9,101,2,9,9,102,3,9,9,1001,9,5,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1001,9,4,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,3,9,4,9,99,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def dp(s):
    if DEBUG:
        print(s)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def read_operand(addr, mode, state):
    ind_addr = state[addr]

    if mode:
        op = state[addr]
        dp("operand = %d. Immediate read from address %d" % (op, addr))
    else:
        op = state[ind_addr]
        dp("operand = %d. Indirect read from address %d" % (op, ind_addr))
    return op


#-------------------------------------------------------------------
# cpu
# Execute the program stored in the state. Starting at address 0.
#-------------------------------------------------------------------
def cpu(state, inputs):
    # Opcodes
    OP_ADD  = 1
    OP_MUL  = 2
    OP_IN   = 3
    OP_OUT  = 4
    OP_JNZ  = 5
    OP_JZ   = 6
    OP_LT   = 7
    OP_EQ   = 8
    OP_HALT = 99

    outputs = 0
    ic = 0
    ip = 0
    done = False

    while not done:
        # Instruction fetch and decode to get op and operand modes.
        instr = state[ip]
        op = instr % 100
        dp("ip: %d, instr: %d" % (ip, instr))
        mode_a = int(instr / 100) & 0x01
        mode_b = int(instr / 1000)  & 0x01
        mode_c = int(instr / 10000) & 0x01

        # Execute
        if op == OP_ADD:
            dp("\nOP_ADD")
            opa = read_operand(ip + 1, mode_a, state)
            opb = read_operand(ip + 2, mode_b, state)
            dst = state[ip + 3]
            dp("Writing %d to state[%d]" % (opa + opb, dst))
            state[dst] = opa + opb
            ip += 4


        if op == OP_MUL:
            dp("\nOP_MUL")
            opa = read_operand(ip + 1, mode_a, state)
            opb = read_operand(ip + 2, mode_b, state)
            dst = state[ip + 3]
            dp("Writing %d to state[%d]" % (opa * opb, dst))
            state[dst] = opa * opb
            ip += 4


        if op == OP_IN:
            dp("\nOP_IN")
            i = inputs[ic]
            ic += 1
            dst = state[ip + 1]
            state[dst] = i
            dp("Got %d. Stored to state[%d]" % (i, dst))
            ip += 2


        if op == OP_OUT:
            dp("\nOP_OUT")
            opa = read_operand(ip + 1, mode_a, state)
            dp("Output: %d" % (opa))
            outputs = opa
            ip += 2


        if op == OP_JNZ:
            dp("\nOP_JNZ")
            opa = read_operand(ip + 1, mode_a, state)
            opb = read_operand(ip + 2, mode_b, state)
            if opa != 0:
                dp("opa != 0, jumping to addr %d" % (opb))
                ip = opb
            else:
                dp("opa == 0, moving to next instruction")
                ip += 3


        if op == OP_JZ:
            dp("\nOP_JZ")
            opa = read_operand(ip + 1, mode_a, state)
            opb = read_operand(ip + 2, mode_b, state)

            if opa == 0:
                ip = opb
                dp("opa == 0, jumping to addr %d" % (opb))
            else:
                dp("opa != 0, moving to next instruction")
                ip += 3


        if op == OP_LT:
            dp("\nOP_LT")
            opa = read_operand(ip + 1, mode_a, state)
            opb = read_operand(ip + 2, mode_b, state)
            dst = state[ip + 3]

            if opa < opb:
                state[dst] = 1
                dp("opa < opb. Writing 1 to state[%d]" % (dst))
            else:
                state[dst] = 0
                dp("opa >= opb. Writing 0 to state[%d]" % (dst))
            ip += 4


        if op == OP_EQ:
            dp("\nOP_EQ")
            opa = read_operand(ip + 1, mode_a, state)
            opb = read_operand(ip + 2, mode_b, state)
            dst = state[ip + 3]

            if opa == opb:
                state[dst] = 1
                dp("opa == opb. Writing 1 to state[%d]" % (dst))
            else:
                state[dst] = 0
                dp("opa != opb. Writing 0 to state[%d]" % (dst))
            ip += 4


        if op == OP_HALT:
            dp("\nOP_HALT")
            done = True

    return outputs


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_signal(prog, phases):
    signal = 0
    for phase in phases:
        tmp_prog = prog[:]
        tmp_inputs = [phase, signal]
        signal = cpu(tmp_prog, tmp_inputs)
    return signal


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def find_max(prog):
    max_signal = 0
    phases = list(itertools.permutations([0, 1, 2, 3, 4]))
    for phase in phases:
        tmp_prog = prog[:]
        signal = get_signal(tmp_prog, phase)
        if signal > max_signal:
            max_signal = signal
            max_phase = phase
    return (max_signal, max_phase)


#-------------------------------------------------------------------
# problem1
# Provide 1 as input.
#-------------------------------------------------------------------
def problem1():
    TEST1 = False

    print("Problem 1")
    test_prog1_1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    test_phase1_1 = [4,3,2,1,0]

    test_prog1_2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
                    101,5,23,23,1,24,23,23,4,23,99,0,0]
    test_phase1_2 = [0,1,2,3,4]

    test_prog1_3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,
                    31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,
                    4,31,99,0,0,0]
    test_phase1_3 = [1,0,4,3,2]

    if (TEST1):
        signal = get_signal(test_prog1_1, test_phase1_1)
        print("Thrust signal from running test 1: %d" % signal)

        signal = get_signal(test_prog1_2, test_phase1_2)
        print("Thrust signal from running test 2: %d" % signal)

        signal = get_signal(test_prog1_3, test_phase1_3)
        print("Thrust signal from running test 3: %d" % signal)

        (s, p) = find_max(test_prog1_1)
        print(s, p)

    else:
        (s, p) = find_max(puzzle_prog)
        print("Max signal %d." % (s))
        print(p)
        print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()

#=======================================================================
