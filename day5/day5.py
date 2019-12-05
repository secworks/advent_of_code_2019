#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 5.
# Based on day2.
#=======================================================================

DEBUG = False

TEST_program = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,7,85,225,1102,67,12,225,102,36,65,224,1001,224,-3096,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1001,17,31,224,1001,224,-98,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,86,19,225,1101,5,27,225,1102,18,37,225,2,125,74,224,1001,224,-1406,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1102,13,47,225,1,99,14,224,1001,224,-98,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,1101,38,88,225,1102,91,36,224,101,-3276,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1101,59,76,224,1001,224,-135,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,101,90,195,224,1001,224,-112,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1102,22,28,225,1002,69,47,224,1001,224,-235,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,226,226,224,102,2,223,223,1006,224,329,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,344,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,359,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,1008,677,226,224,1002,223,2,223,1006,224,389,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,404,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,419,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,434,1001,223,1,223,8,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,464,101,1,223,223,1007,226,677,224,1002,223,2,223,1006,224,479,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,509,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,524,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,584,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,599,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,1107,226,677,224,102,2,223,223,1006,224,629,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]


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
def cpu(state):
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
            i = int(input("Input: "))
            dst = state[ip + 1]
            state[dst] = i
            dp("Got %d. Stored to state[%d]" % (i, dst))
            ip += 2


        if op == OP_OUT:
            dp("\nOP_OUT")
            opa = read_operand(ip + 1, mode_a, state)
            print("Output: %d" % (opa))
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

    return state


#-------------------------------------------------------------------
# problem1
# Provide 1 as input.
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    test1_1 = [3,0,4,0,99, 0, 0, 0]
    test1_2 = [1002,4,3,4,33, 0, 0, 0]

    TEST = False

    if TEST:
        print("Running test1_1")
        res_state = cpu(test1_1)
        print("test1_1 done.")
        print("")

        print("Running test1_2")
        res_state = cpu(test1_2)
        print("test1_2 done.")
        print("")
        print(res_state)

    else:
        print("Running TEST program.")
        res_state = cpu(TEST_program[:])
        print("TEST program done.")
        print("")


#-------------------------------------------------------------------
# problem2
# Provide 5 as input.
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    # Test of EQ and LT
    test2_1 = [3,9,8,9,10,9,4,9,99,-1,8]
    test2_2 = [3,9,7,9,10,9,4,9,99,-1,8]
    test2_3 = [3,3,1108,-1,8,3,4,3,99]
    test2_4 = [3,3,1107,-1,8,3,4,3,99]

    # Test of JZ and JNZ
    test2_5 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]

    TEST = False

    if TEST:
        print("Running test2_1")
        res_state = cpu(test2_1)
        print("test2_1 done.")
        print("")

        print("Running test2_2")
        res_state = cpu(test2_2)
        print("test2_2 done.")
        print("")

        print("Running test2_3")
        res_state = cpu(test2_3)
        print("test2_3 done.")
        print("")

        print("Running test2_4")
        res_state = cpu(test2_4)
        print("test2_4 done.")
        print("")

        print("Running test2_5")
        res_state = cpu(test2_5)
        print("test2_5 done.")
        print("")

    else:
        print("Running TEST program.")
        res_state = cpu(TEST_program[:])
        print("TEST program done.")
        print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
