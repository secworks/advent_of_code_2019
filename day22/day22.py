#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 22.
#=======================================================================

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    indata = []
    with open(filename,'r') as f:
        line = f.read()
    return [int(x) for x in line.strip()]


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def find_card(deck, card):
    for i in range(len(deck)):
        if deck[i] == card:
            return i


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def increment(deck, inc):
    orig_len = len(deck)
    tmp = [0] * orig_len
    ptr = 0
    while len(deck) > 0:
        e = deck.pop(0)
        tmp[ptr] = e
        ptr = (ptr + inc) % orig_len
    return tmp


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def shuffle(deck, instructions):
    for i in instructions:
        print(deck)
        if "deal into new stack" in i:
            print("Reversing")
            deck.reverse()


        elif "cut" in i:
            pos = int(i.split(" ")[1])
            print("Doing cut at pos %d" % pos)
            deck = deck[pos:] + deck[:pos]


        elif "deal with increment" in i:
            inc = int(i.split(" ")[3])
            print("Deal with increment at %d" % inc)
            deck = increment(deck, inc)

        else:
            print("Unrecognized command: %s" % i)
    return deck


#-------------------------------------------------------------------
# problem1
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    test_deck1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    test_instr1 = ["deal with increment 7", "deal into new stack",
                   "deal into new stack"]

    test_instr2 = ["cut 6", "deal with increment 7",
                   "deal into new stack"]

    test_instr3 = ["deal with increment 7", "deal with increment 9",
                   "cut -2"]

    test_instr4 = ["deal into new stack", "cut -2",
                   "deal with increment 7", "cut 8",
                   "cut -4", "deal with increment 7", "cut 3",
                   "deal with increment 9", "deal with increment 3",
                   "cut -1"]

#    assert(shuffle(test_deck1[:], test_instr1) == [0,3,6,9,2,5,8,1,4,7])
#    assert(shuffle(test_deck1[:], test_instr2) == [3,0,7,4,1,8,5,2,9,6])
#    assert(shuffle(test_deck1[:], test_instr3) == [6,3,0,7,4,1,8,5,2,9])
#    assert(shuffle(test_deck1[:], test_instr4) == [9,2,5,8,1,4,7,0,3,6])
    print("")

#-------------------------------------------------------------------
# problem2
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
