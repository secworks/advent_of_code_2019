#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 9. Based in day7_problem2.py
#=======================================================================

DEBUG = True

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    i = []
    with open(filename,'r') as f:
        for line in f:
            l = line.strip().split(",")

    for s in l:
        i.append(int(s))
    return i


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def dp(s):
    if DEBUG:
        print(s)

#-------------------------------------------------------------------
# read_operand
#-------------------------------------------------------------------
def read_operand(addr, mode, state, rb):
    if mode == 2:
        ind_addr = state[addr] + rb
        op = state[ind_addr]
        dp("operand = %d. Relative read from address %d" % (op, ind_addr))

    elif mode == 1:
        ind_addr = state[addr]
        op = state[ind_addr]
        dp("operand = %d. Position read from address %d" % (op, ind_addr))

    else:
        op = state[addr]
        dp("operand = %d. Immediate read from address %d" % (op, addr))
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
        dp("ip: %d, rb: %d, instr: %d" % (ip, rb, instr))
        if len(str(instr)) > 2:
            mode_a = int(str(instr)[ / 100) & 0x03
        mode_b = int(instr / 1000)  & 0x03
        mode_c = int(instr / 10000) & 0x03

        # Operand fetch

        # Execute
        if op == OP_ADD:
            dp("\nOP_ADD")
            opa = read_operand(ip + 1, mode_a, mem_state, rb)
            opb = read_operand(ip + 2, mode_b, mem_state, rb)
            dst = read_operand(ip + 3, mode_c + 1, mem_state, rb)
            dp("Writing %d to state[%d]" % (opa + opb, dst))
            mem_state[dst] = opa + opb
            ip += 4

        elif op == OP_MUL:
            dp("\nOP_MUL")
            opa = read_operand(ip + 1, mode_a, mem_state, rb)
            opb = read_operand(ip + 2, mode_b, mem_state, rb)
            dst = read_operand(ip + 3, mode_c + 1, mem_state, rb)
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
            if opa != 0:
                dp("opa != 0, jumping to addr %d" % (opb))
                ip = opb
            else:
                dp("opa == 0, moving to next instruction")
                ip += 3

        elif op == OP_JZ:
            dp("\nOP_JZ")
            if opa == 0:
                ip = opb
                dp("opa == 0, jumping to addr %d" % (opb))
            else:
                dp("opa != 0, moving to next instruction")
                ip += 3

        elif op == OP_LT:
            dp("\nOP_LT")
            if opa < opb:
                mem_state[dst] = 1
                dp("opa < opb. Writing 1 to state[%d]" % (dst))
            else:
                mem_state[dst] = 0
                dp("opa >= opb. Writing 0 to state[%d]" % (dst))
            ip += 4

        elif op == OP_EQ:
            dp("\nOP_EQ")
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
        print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def run_program(program, inp):
    my_program = program[:]
    # Extend with extra memory initialized to zero.
    my_program.extend([0] * 1024)

    # Initialize the context.
    ctx = ("init", my_program, 0, 0)
    status = "init"
    response = []

    # Run the program until done or error.
    # Stora any output.
    while status != "done":
        (status, outdata, ctx) = cpu(ctx, 0)
        if status == "out":
            response.append(outdata)
            dp(outdata)

        if status == "error":
            return (False, response)

    return (True, response)


#-------------------------------------------------------------------
# problem1
#-------------------------------------------------------------------
def problem1():
    TEST1 = True
    tprog1_1 = [109,1,204,-1,1001,100,1,100,99,1008,100,16,101,1006,101,0,99]
    tprog1_2 = [1102,34915192,34915192,7,4,7,99,0]
    tprog1_3 = [104,1125899906842624,99]

#    my_program = get_input("day9_input.txt")
#    print(my_program)
    print("Problem 1")

    if TEST1:
        res = run_program(tprog1_1, [])
        print("Result: ", res)
#        res = run_program(tprog1_2)
#        res = run_program(tprog1_3)

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
