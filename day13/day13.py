#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 9. Based in day7_problem2.py
#=======================================================================

DEBUG = True

import itertools

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    with open(filename,'r') as f:
        for line in f:
            l = line.strip().split(",")
    return [int(x) for x in l]


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def dp(s):
    if DEBUG:
        print(s)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def read_operand(addr, mode, state, rb):

    if mode == 2:
        ind_addr = state[addr + rb]
        op = state[ind_addr]
        dp("operand = %d. Relative read from address %d" % (op, addr))

    elif mode == 1:
        op = state[addr]
        dp("operand = %d. Immediate read from address %d" % (op, addr))

    else:
        ind_addr = state[addr + rb]
        op = state[ind_addr]
        dp("operand = %d. Position read from address %d" % (op, ind_addr))

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
    OP_RB   = 9
    OP_HALT = 99

    (exe_state, mem_state, ip, rb) = ctx
    done = False

    if exe_state == "init":
        ip = 0
        rb = 0
        exe_state = "running"

    while not done:
        # Instruction fetch and decode to get op and operand modes.
        instr = mem_state[ip]
        op = instr % 100
        dp("ip: %d, instr: %d" % (ip, instr))
        mode_a = int(instr / 100) & 0x03
        mode_b = int(instr / 1000)  & 0x03
        mode_c = int(instr / 10000) & 0x03

        # Execute
        if op == OP_ADD:
            dp("\nOP_ADD")
            opa = read_operand(ip + 1, mode_a, mem_state, rb)
            opb = read_operand(ip + 2, mode_b, mem_state, rb)
            dst = mem_state[ip + 3]
            dp("Writing %d to state[%d]" % (opa + opb, dst))
            mem_state[dst] = opa + opb
            ip += 4


        elif op == OP_MUL:
            dp("\nOP_MUL")
            opa = read_operand(ip + 1, mode_a, mem_state, rb)
            opb = read_operand(ip + 2, mode_b, mem_state, rb)
            dst = mem_state[ip + 3]
            dp("Writing %d to state[%d]" % (opa * opb, dst))
            mem_state[dst] = opa * opb
            ip += 4


        elif op == OP_IN:
            dp("\nOP_IN")
            if exe_state == "running":
                dp("Need to get input.")
                return ("in", 0, ("wait_in", mem_state, ip, rb))
            else:
                dp("Input received, continuing.")
                exe_state = "running"
                i = indata
                dst = mem_state[ip + 1]
                mem_state[dst] = i
                dp("Got %d. Stored to state[%d]" % (i, dst))
                ip += 2


        elif op == OP_OUT:
            dp("\nOP_OUT")
            opa = read_operand(ip + 1, mode_a, mem_state, rb)
            if exe_state == "running":
                dp("Need to send output.")
                return ("out", opa, ("wait_out", mem_state, ip, rb))
            else:
                dp("Output sent, continuing.")
                exe_state = "running"
                dp("Output: %d" % (opa))
                ip += 2


        elif op == OP_JNZ:
            dp("\nOP_JNZ")
            opa = read_operand(ip + 1, mode_a, mem_state, rb)
            opb = read_operand(ip + 2, mode_b, mem_state, rb)
            if opa != 0:
                dp("opa != 0, jumping to addr %d" % (opb))
                ip = opb
            else:
                dp("opa == 0, moving to next instruction")
                ip += 3


        elif op == OP_JZ:
            dp("\nOP_JZ")
            opa = read_operand(ip + 1, mode_a, mem_state, rb)
            opb = read_operand(ip + 2, mode_b, mem_state, rb)

            if opa == 0:
                ip = opb
                dp("opa == 0, jumping to addr %d" % (opb))
            else:
                dp("opa != 0, moving to next instruction")
                ip += 3


        elif op == OP_LT:
            dp("\nOP_LT")
            opa = read_operand(ip + 1, mode_a, mem_state, rb)
            opb = read_operand(ip + 2, mode_b, mem_state, rb)
            dst = state[ip + 3]

            if opa < opb:
                mem_state[dst] = 1
                dp("opa < opb. Writing 1 to state[%d]" % (dst))
            else:
                mem_state[dst] = 0
                dp("opa >= opb. Writing 0 to state[%d]" % (dst))
            ip += 4


        elif op == OP_EQ:
            dp("\nOP_EQ")
            opa = read_operand(ip + 1, mode_a, mem_state, rb)
            opb = read_operand(ip + 2, mode_b, mem_state, rb)
            dst = mem_state[ip + 3]

            if opa == opb:
                mem_state[dst] = 1
                dp("opa == opb. Writing 1 to state[%d]" % (dst))
            else:
                mem_state[dst] = 0
                dp("opa != opb. Writing 0 to state[%d]" % (dst))
            ip += 4


        elif op == OP_RB:
            dp("\nOP_RB")
            opa = read_operand(ip + 1, mode_a, mem_state, rb)
            dp("Setting relative base to: %d" % (opa))
            rb = opa
            ip += 2


        elif op == OP_HALT:
            dp("\nOP_HALT")
            done = True
            return ("done", 0, (exe_state, mem_state, ip, rb))

        else:
            dp("\nOP_UNKNOWN")
            done = True
            return ("error", 0, (exe_state, mem_state, ip, rb))


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def run_program(program):
    my_program = program[:]
    my_program.extend([0] * 1024)
    ctx = ("init", my_program, 0, 0)
    status = "init"
    response = 0

    while status != "done":
        (status, outdata, ctx) = cpu(ctx, 0)
        if status == "out":
            response = outdata
            dp(outdata)

        if status == "error":
            return False

    return response


#-------------------------------------------------------------------
# problem1
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    my_program = get_input("day13_input.txt")
    print(my_program)
    print("")


#-------------------------------------------------------------------
# problem2
#-------------------------------------------------------------------
def problem2():
    TEST1 = True

    print("Problem 2")
    print("")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
