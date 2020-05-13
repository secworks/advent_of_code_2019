#!/usr/bin/env python3
#=======================================================================
#
# intcode.py
# ----------
# A Python implementation of the Intcode computer.
#
#=======================================================================

import sys

#-------------------------------------------------------------------
#-------------------------------------------------------------------
class Intcode():
    """AoC 2019 Intcode computer."""

    def __init__(self, mem_size = 100, debug = True):
        if (debug):
            print("Initializing a new Incode computer.")
        self.debug = debug
        self.mem = [0] * mem_size
        self.reset()


    def reset(self):
        self.ip    = 0
        self.base  = 0
        self.state = "idle"


    def load(self, program):
        if self.debug:
            print("Loading program:", program)

        if (len(program) > len(self.mem)):
            print("Program too large to fit in memory.")
            return ("error", 1)

        for i in range(len(program)):
            self.mem[i] = program[i]
        return (self.state, 0)


    def log(self, s):
        if self.debug:
            print(s)


    def run(self, indata = None):
        if (self.state == "idle"):
            self.log("Starting to execute program in memory")
            self.state = "run"
        else:
            self.log("Continue to execute program in memory.")


        while(self.state != "halt"):
            opcode = self.mem[self.ip]
            param1 = self.mem[self.ip + 1]
            param2 = self.mem[self.ip + 2]
            param3 = self.mem[self.ip + 3]

            if (opcode == 1):
                self.log("Add instruction executed.")
                self.mem[param3] = self.mem[param1] + self.mem[param2]
                self.ip += 4


            elif (opcode == 2):
                self.log("Mult instruction executed.")
                self.mem[param3] = self.mem[param1] * self.mem[param2]
                self.ip += 4


            elif (opcode == 3):
                if (self.state == "run"):
                    self.log("Input instruction executed. Require indata")
                    self.state == "input"
                    return(self.state, 0)

                elif (self.state == "input"):
                    self.log("Input instruction executed. Indata %d received." % indata)
                    if (indata == None):
                        print("Error: No input given.")
                        self.state == "error"
                        return(self.state, 1)
                    self.mem[param1] = indata
                    self.state == "run"
                    self.ip += 2


            elif (opcode == 4):
                if (self.state == "run"):
                    self.log("Output instruction executed. Outputting data.")
                    self.state == "output"
                    return(self.state, self.mem[param1])
                elif (self.state == "output"):
                    self.log("Output instruction executed. Returned from output.")
                    self.state == "run"
                    self.ip += 2


            elif (opcode == 99):
                self.log("Halt instruction executed.")
                self.state = "halt"
                return (self.state, 0)


            else:
                self.log("Unknown instruction %d executed" % opcode)
                self.state = "unknown"
                Return (self.state, opcode)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def run_day2_1():
    program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,6,23,27,1,5,27,31,2,31,9,35,1,35,5,39,1,39,5,43,1,43,10,47,2,6,47,51,1,51,5,55,2,55,6,59,1,5,59,63,2,63,6,67,1,5,67,71,1,71,6,75,2,75,10,79,1,79,5,83,2,83,6,87,1,87,5,91,2,9,91,95,1,95,6,99,2,9,99,103,2,9,103,107,1,5,107,111,1,111,5,115,1,115,13,119,1,13,119,123,2,6,123,127,1,5,127,131,1,9,131,135,1,135,9,139,2,139,6,143,1,143,5,147,2,147,6,151,1,5,151,155,2,6,155,159,1,159,2,163,1,9,163,0,99,2,0,14,0]
    program[1] = 12
    program[2] = 2

    print("Running program for day2, problem 1.")
    my_intcode = Intcode(len(program), debug=False)
    my_response = my_intcode.load(program)
    (response, value) = my_intcode.run()
    if (my_intcode.mem[0] ==  10566835):
        print("Correct answer for day2 problem 1 received.")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def run_test(prog, expected):
    my_intcode = Intcode(16)
    my_response = my_intcode.load(prog)
    (response, value) = my_intcode.run()
    if (my_response == "unknown"):
        print("Unknown instruction executed")
    else:
        if (my_intcode.mem[0 : len(prog)] == expected):
            print("Correct result received.")
        else:
            print("Incorrect result received.")
            print("Exp:", expected)
            print("Got:", my_intcode.mem[0 : len(prog)])
    print("")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def selftest():
    run_test([1,0,0,0,99],          [2,0,0,0,99])
    run_test([2,3,0,3,99],          [2,3,0,6,99])
    run_test([2,4,4,5,99,0],        [2,4,4,5,99,9801])
    run_test([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])
    run_day2_1()

#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(selftest())

#=======================================================================
# EOF intcode.py
#=======================================================================
