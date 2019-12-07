#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 7.
# Based on day5.
#=======================================================================

DEBUG = False


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
            print("Output: %d" % (opa))
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
# problem1
# Provide 1 as input.
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    test_prog1_1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    test_phase1_1 = [4,3,2,1,0]

    signal = get_signal(test_prog1_1, test_phase1_1)
    print("Thrust signal from running test 1: %d" % signal)


#-------------------------------------------------------------------
# problem2
# Provide 5 as input.
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
