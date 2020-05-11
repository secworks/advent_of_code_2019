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
        self.mem = [0] * mem_size
        self.debug = debug
        self.pc = 0
        self.base = 0


    def load(self, program):
        assert (len(program) <= len(self.mem)), "Program doesn't fit in memory."
        return 1

        for b in program:
            pass

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def selftest():
    my_intcode = Intcode(2)
    my_intcode.load([1, 2, 3, 4])

#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(selftest())

#=======================================================================
# EOF intcode.py
#=======================================================================
