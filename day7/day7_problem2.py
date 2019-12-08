#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 7, problem 2.
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
def cpu(ctx, indata):
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

    (exe_state, mem_state, ip) = ctx
    done = False

    if exe_state == "init":
        ip = 0
        exe_state = "running"

    while not done:
        # Instruction fetch and decode to get op and operand modes.
        instr = mem_state[ip]
        op = instr % 100
        dp("ip: %d, instr: %d" % (ip, instr))
        mode_a = int(instr / 100) & 0x01
        mode_b = int(instr / 1000)  & 0x01
        mode_c = int(instr / 10000) & 0x01

        # Execute
        if op == OP_ADD:
            dp("\nOP_ADD")
            opa = read_operand(ip + 1, mode_a, mem_state)
            opb = read_operand(ip + 2, mode_b, mem_state)
            dst = mem_state[ip + 3]
            dp("Writing %d to state[%d]" % (opa + opb, dst))
            mem_state[dst] = opa + opb
            ip += 4


        if op == OP_MUL:
            dp("\nOP_MUL")
            opa = read_operand(ip + 1, mode_a, mem_state)
            opb = read_operand(ip + 2, mode_b, mem_state)
            dst = mem_state[ip + 3]
            dp("Writing %d to state[%d]" % (opa * opb, dst))
            mem_state[dst] = opa * opb
            ip += 4


        if op == OP_IN:
            dp("\nOP_IN")
            if exe_state == "running":
                dp("Need to get input.")
                return ("in", 0, ("wait_in", mem_state, ip))
            else:
                dp("Input received, continuing.")
                exe_state = "running"
                i = indata
                dst = mem_state[ip + 1]
                mem_state[dst] = i
                dp("Got %d. Stored to state[%d]" % (i, dst))
                ip += 2


        if op == OP_OUT:
            dp("\nOP_OUT")
            opa = read_operand(ip + 1, mode_a, mem_state)
            if exe_state == "running":
                dp("Need to send output.")
                return ("out", opa, ("wait_out", mem_state, ip))
            else:
                dp("Output sent, continuing.")
                exe_state = "running"
                dp("Output: %d" % (opa))
                ip += 2


        if op == OP_JNZ:
            dp("\nOP_JNZ")
            opa = read_operand(ip + 1, mode_a, mem_state)
            opb = read_operand(ip + 2, mode_b, mem_state)
            if opa != 0:
                dp("opa != 0, jumping to addr %d" % (opb))
                ip = opb
            else:
                dp("opa == 0, moving to next instruction")
                ip += 3


        if op == OP_JZ:
            dp("\nOP_JZ")
            opa = read_operand(ip + 1, mode_a, mem_state)
            opb = read_operand(ip + 2, mode_b, mem_state)

            if opa == 0:
                ip = opb
                dp("opa == 0, jumping to addr %d" % (opb))
            else:
                dp("opa != 0, moving to next instruction")
                ip += 3


        if op == OP_LT:
            dp("\nOP_LT")
            opa = read_operand(ip + 1, mode_a, mem_state)
            opb = read_operand(ip + 2, mode_b, mem_state)
            dst = state[ip + 3]

            if opa < opb:
                mem_state[dst] = 1
                dp("opa < opb. Writing 1 to state[%d]" % (dst))
            else:
                mem_state[dst] = 0
                dp("opa >= opb. Writing 0 to state[%d]" % (dst))
            ip += 4


        if op == OP_EQ:
            dp("\nOP_EQ")
            opa = read_operand(ip + 1, mode_a, mem_state)
            opb = read_operand(ip + 2, mode_b, mem_state)
            dst = mem_state[ip + 3]

            if opa == opb:
                mem_state[dst] = 1
                dp("opa == opb. Writing 1 to state[%d]" % (dst))
            else:
                mem_state[dst] = 0
                dp("opa != opb. Writing 0 to state[%d]" % (dst))
            ip += 4


        if op == OP_HALT:
            dp("\nOP_HALT")
            done = True
            return ("done", 0, (exe_state, mem_state, ip))


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_signal_feedback(program, phases):
    ctx_a = ("init", program[:], 0)
    ctx_b = ("init", program[:], 0)
    ctx_c = ("init", program[:], 0)
    ctx_d = ("init", program[:], 0)
    ctx_e = ("init", program[:], 0)

    loop_state = "init"
    a_in = 0
    b_in = 0
    c_in = 0
    d_in = 0
    e_in = 0

    while loop_state != "done":
        if loop_state == "init":
            dp("Init of amplifier A")
            (status, outdata, ctx_a) = cpu(ctx_a, 0)
            (status, outdata, ctx_a) = cpu(ctx_a, phases[0])
        dp("Running amplifier A with input %d" % a_in)
        (status, outdata, ctx_a) = cpu(ctx_a, a_in)

        if status == "out":
            b_in = outdata

        if loop_state == "init":
            dp("Init of amplifier B")
            (status, outdata, ctx_b) = cpu(ctx_b, 0)
            (status, outdata, ctx_b) = cpu(ctx_b, phases[1])
        dp("Running amplifier B with input %d" % b_in)
        (status, outdata, ctx_b) = cpu(ctx_b, b_in)

        if status == "out":
            c_in = outdata

        if loop_state == "init":
            dp("Init of amplifier C")
            (status, outdata, ctx_c) = cpu(ctx_c, 0)
            (status, outdata, ctx_c) = cpu(ctx_c, phases[2])
        dp("Running amplifier C with input %d" % c_in)
        (status, outdata, ctx_c) = cpu(ctx_c, c_in)

        if status == "out":
            d_in = outdata

        if loop_state == "init":
            dp("Init of amplifier D")
            (status, outdata, ctx_d) = cpu(ctx_d, 0)
            (status, outdata, ctx_d) = cpu(ctx_d, phases[3])
        dp("Running amplifier D with input %d" % d_in)
        (status, outdata, ctx_d) = cpu(ctx_d, d_in)

        if status == "out":
            e_in = outdata

        if loop_state == "init":
            dp("Init of amplifier E")
            (status, outdata, ctx_e) = cpu(ctx_e, 0)
            (status, outdata, ctx_e) = cpu(ctx_e, phases[4])
        dp("Running amplifier E with input %d" % e_in)
        (status, outdata, ctx_e) = cpu(ctx_e, e_in)

        if status == "out":
            e_out = outdata
            a_in = e_out

        if status == "done":
            dp("Received halt from Amplifier E. We are done.")
            loop_state = "done"
        else:
            loop_state = "looping"

    return e_out


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def find_max(program):
    max_signal = 0
    phases = list(itertools.permutations([5, 6, 7, 8, 9]))
    for phase in phases:
        signal = get_signal_feedback(program, phase)
        if signal > max_signal:
            max_signal = signal
            max_phase = phase
    return (max_signal, max_phase)

#-------------------------------------------------------------------
# problem1
#-------------------------------------------------------------------
def problem2():
    TEST1 = False

    print("Problem 2")
    signal, phase = find_max(puzzle_prog)
    print("received signal: %d" % signal)
    print("Given by phase: ", phase)
    print("")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem2()

#=======================================================================
