#!/usr/bin/env python3

# Solutions to Advent of Code 2019, day 1.

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(int(line.strip()))
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def round_down(n):
    return int(n / 3) - 2


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def additional_fuel(n):
    s = 0
    p = n
    while round_down(p) > 0:
        p = round_down(p)
#        print("n = %d, p = %d" % (n, p))
        s += p
    return s


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("Testing the run_down function.")
    test_data1 = [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
    for n, r in test_data1:
        print("round_down(%d) = %d, expected %d" % (n, round_down(n), r))

    my_list = get_input("input_d1_p1.txt")
#    print(my_list)

    my_sum = 0
    for n in my_list:
        my_sum += round_down(n)
    print("Sum of rounded down values: %d" % (my_sum))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("Testing the additional_fuel function.")
    test_data1 = [(12, 2), (1969, 966), (100756, 50346)]
    for n, r in test_data1:
        print("additional_fuel(%d) = %d, expected %d" %\
              (n, additional_fuel(n), r))

    my_list = get_input("input_d1_p1.txt")

    my_sum = 0
    for n in my_list:
        my_sum += additional_fuel(n)
    print("Sum of additional fuel: %d" % (my_sum))
    print("")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()
