#!/usr/bin/env python3
#===================================================================
# Solutions to Advent of Code 2019, day 6.
#===================================================================

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            m = line.strip().split(')')
            [c, o] = m
            l.append((c, o))
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def build_tree(orbit_name, depth, orbits):
    direct_orbits = []
    other_orbits = []
    orbit_list = []

    for o in orbits:
        name, orbit = o
        if name == orbit_name:
            direct_orbits.append(orbit)
        else:
            other_orbits.append(o)

    for name in direct_orbits:
        orbit_list.append(build_tree(name, depth + 1, other_orbits))

    return (orbit_name, depth, orbit_list)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_depth(n):
    name, depth, nodes = n
    nd = 0
    for node in nodes:
        nd += get_depth(node)
    return depth + nd

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    my_input = get_input("day6_input.txt")

    my_orbits = build_tree("COM", 0, my_input)
    print("Total number of orbits: %d" % (get_depth(my_orbits)))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()
#===================================================================
