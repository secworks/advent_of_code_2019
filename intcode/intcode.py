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


    def run(self, indata = None):
        if (self.debug):
            if (self.state == "idle"):
                print("Starting to execute program in memory")
                self.state = "run"
            else:
                print("Continue to execute program in memory.")

        while(self.state != "halt"):
            opcode = self.mem[self.ip]
            param1 = self.mem[self.ip + 1]
            param2 = self.mem[self.ip + 2]
            param3 = self.mem[self.ip + 3]

            if (opcode == 1):
                if (self.debug):
                    print("Add instruction executed.")
                self.mem[param3] = self.mem[param1] + self.mem[param2]
                self.ip += 4


            elif (opcode == 2):
                if (self.debug):
                    print("Mult instruction executed.")
                self.mem[param3] = self.mem[param1] * self.mem[param2]
                self.ip += 4


            elif (opcode == 99):
                if (self.debug):
                    print("Halt instruction executed.")
                self.state = "halt"
                return (self.state, 0)


            else:
                if (self.debug):
                    print("Unknown instruction %d executed" % opcode)
                self.state = "unknown"
                return (self.state, opcode)



#-------------------------------------------------------------------
#-------------------------------------------------------------------
def selftest():
    my_intcode = Intcode(10)
    my_response = my_intcode.load([1,0,0,0,99])
    my_response = my_intcode.run()
    print(my_response)
    print(my_intcode.mem)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(selftest())

#=======================================================================
# EOF intcode.py
#=======================================================================
